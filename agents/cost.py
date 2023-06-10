import utils.utils as utils
import torch
import numpy as np

class Cost():
    """ Class for approximating the cost function. """

    K = 5 # Number of update steps to perform each iteration

    def __init__(self, action_size, state_size, hidden_layer_size, hidden_layers):
        """ Initialize the network and optimizer. """
        self.net = utils.generate_simple_network(state_size + action_size, 1, hidden_layer_size, hidden_layers)
        self.optimizer = torch.optim.Adam(self.net.parameters(), lr=0.0025)

        self.pick_net = utils.generate_simple_network(state_size + action_size -4, 1, hidden_layer_size, hidden_layers)
        self.pick_optimizer = torch.optim.Adam(self.pick_net.parameters(), lr=0.005)
        self.pick_ioc_lik = []
        self.ioc_lik = []

    def non_linear_ioc(self, d_demo, d_samp, it, agent):
        """ Non-linear IOC with stochastic patterns.

        Algorithm 2 from paper.
        """
        cum_ioc_like = 0
        cum_pick_ioc_like = 0
        for iter in range(50 if it < 10 else self.K):
            # Sample demonstration batch Dˆdemo ⊂ Ddemo
            d_s_demo = d_demo.sample(20)

            # Sample background batch Dˆsamp ⊂ Dsamp
            d_s_samp = d_samp.sample(20)
            # Append demonstration batch to background batch:
            # Dˆsamp ← Dˆdemo ∪ Dˆsamp
            d_s_samp.extend(d_s_demo)
            # Estimate dLIOC dθ (θ) using Dˆdemo and Dˆsamp
            samp_probs = d_s_samp.probs
            p_samp_probs = d_s_samp.pick_probs
#            t_samp_probs = agent.get_probs(torch.tensor(d_s_samp.states[:,:14], dtype=torch.float32), False).numpy()
#            samp_probs = [0] * 20
#            for i in range(20):
#                samp_probs[i] = t_samp_probs[i,int(d_s_samp.actions[i])]
#            samp_probs = samp_probs + [1] * 20
#            samp_probs_t = torch.tensor(samp_probs, dtype=torch.float32)

#            samp_probs = np.concatenate(agent.get_probs(torch.tensor(d_s_samp.states[:,:14], dtype=torch.float32), False).numpy()[d_s_samp.actions], np.ones(20))
            samp_probs_t = torch.tensor(samp_probs, dtype=torch.float32)
            p_samp_probs_t = torch.tensor(p_samp_probs, dtype=torch.float32)

            # z = [1/k * Sigma_k(qκ(τ))]^-1
            # L_ioc = 1/N * Sigma_demo(cost(τ)) + log( 1/M * Sigma_samp(z * exp(-cost(τ)) ) )
            #if iter % 5 == 0:
            samp_costs = self.get_cost(torch.tensor(d_s_samp.states, dtype=torch.float32))
            demo_costs = self.get_cost(torch.tensor(d_s_demo.states, dtype=torch.float32))

            ioc_lik = torch.mean( demo_costs ) + torch.log( torch.mean( torch.exp( -samp_costs ) / (samp_probs_t + 1e-7)) )

            # Update parameters θ using gradient dLIOC dθ (θ)
            self.optimizer.zero_grad()
            ioc_lik.backward()
            self.optimizer.step()
        print(samp_costs)
        print(demo_costs)
#        print(d_s_demo.states)

            p_samp_probs = agent.get_pick_probs(torch.tensor(d_s_samp.states[:,:12], dtype=torch.float32), False).numpy()
            samp_probs = [0] * 20
            for i in range(20):
                if d_s_samp.states[i,12] == 1:
                    samp_probs[i] = p_samp_probs[i][0]
                else:
                    samp_probs[i] = p_samp_probs[i][1]
            p_samp_probs = samp_probs + [1] * 20
            p_samp_probs_t = torch.tensor(p_samp_probs, dtype=torch.float32)
            p_samp_costs = self.get_pick_cost(torch.tensor(d_s_samp.states[:,:14], dtype=torch.float32))
            p_demo_costs = self.get_pick_cost(torch.tensor(d_s_demo.states[:,:14], dtype=torch.float32))

            p_ioc_lik = torch.mean( p_demo_costs ) + torch.log( torch.mean( torch.exp( -p_samp_costs ) / (p_samp_probs_t  + 1e-7)) )

            # Update parameters θ using gradient dLIOC dθ (θ)
            self.pick_optimizer.zero_grad()
            p_ioc_lik.backward()
            self.pick_optimizer.step()

            cum_ioc_like += ioc_lik.item()
            cum_pick_ioc_like = p_ioc_lik.item()
        print(samp_costs)
        print(demo_costs)
#        print(p_samp_costs)
#        print(p_demo_costs)
#        print(d_s_demo.states)
#        print(d_s_samp.states)
        self.pick_ioc_lik.append(cum_pick_ioc_like)
        self.ioc_lik.append(cum_ioc_like)

    def get_cost(self, x):
        """ Get the cost of a given state-action pair. """
        return torch.sigmoid(self.forward(x))

    def get_pick_cost(self, x):
        """ Get the cost of a given state-action pair. """
        return torch.sigmoid(self.pick_net.forward(x))

    def forward(self, x):
        """ Send data through the network. """
        return self.net.forward(x)

    def save(self, path):
        """ Save the model.

        Inputs:
        path - path to file to save network in
        """
        torch.save(self.net.state_dict(), path)