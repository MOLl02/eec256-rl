
from .random_agent import RandomAgent
import gymnasium as gym
import numpy as np
from utils.utils import normalize_states
import time

class ControlEnv():
    """ Interface for our RL agent to interact with the enviroment. """

    NUM_RND_ACTIONS = 50 # Number of random actions upon state reset

    def __init__(self, add_randomness=False):
        """
        Random agent will be used to randomly initialize the state.
        """
        self.env = gym.make('FetchPickAndPlace-v2', max_episode_steps=100, render_mode = "human")
        self.count = 0
        if add_randomness:
            self.random_agent = RandomAgent(self.env.action_space.n)
        else:
            self.random_agent = None

    @property
    def action_space(self):
        return 4

    @property
    def observation_space(self):
        return 24

    def step(self, seg, action):
        """ Take one action in the simulation.

        Inputs:
        action - action for the agent to take
               - encoded as [segment, dx, dy]

        Outputs:
        observation - state of enviroment following the action
        reward - reward from the prior action
        done - is episode complete
        """
        observation, reward, done = self.do_actions(seg, action)
        return observation, reward, done

    def do_actions(self, seg, action, jitter=False):

        # First move to picked location
        if seg == 1:
            seg = 3
        elif seg == 2:
            seg = 4
        elif seg == 3:
            seg = 7
        new_x, new_y, _ = self.env.get_rope_pos(seg)
        curr_x, curr_y, _ = self.env.get_gripper_xpos()
        while (curr_x > new_x + 0.001) or (curr_x < new_x - 0.001) or (curr_y > new_y + 0.001) or (curr_y < new_y - 0.001):
            curr_x, curr_y, _ = self.env.get_gripper_xpos()
            move_x = min(1, (new_x - curr_x)*20)
            move_y = min(1, (new_y - curr_y)*20)
            self.env.step(np.array([move_x, move_y, 0, 0]))
        # Then lower
        self.env.step(np.array([0, 0, -0.75, 0]))
        # Then move
        dx = 0
        dy = 0
        if action == 0:
            dx = 1
        if action == 1:
            dx = -1
        if action == 2:
            dy = 1
        if action == 3:
            dy = -1
        dx = dx/20
        dy = dy/20
        if jitter:
            dx = dx/5
            dy = dy/5
        for i in range(20):
            self.env.step(np.array([dx, dy, 0, 0])) 

        # Then raise
        self.reset_gripper_height()
        self.count += 1
        state = self.get_rope_states() 

        done = self.count > 50 or state[0] < 1.23 or state[6] > 1.47
        for i in range(1,8,2):
            if state[i] < 0.63 or state[i] > .87:
                done = True

        normalize_states(state)

        return state, 0, done

    def get_rope_states(self):
        state = []
        for i in [0,3,4,7]:
            x, y, _ = self.env.get_rope_pos(i)
            state.append(x)
            state.append(y)
        state = state + 4*[0]
        return np.array(state)

    def reset_gripper_height(self):
        _, _, curr_z = self.env.get_gripper_xpos()
        new_z = 0.475
        while (curr_z > new_z + 0.001) or (curr_z < new_z - 0.001):
            _, _, curr_z = self.env.get_gripper_xpos()
            move_z = min(1, (new_z - curr_z)*20)
            self.env.step(np.array([0, 0, move_z, 0]))

    def reset(self, jitter=False):
        """ Reset the enviroment.

        Outputs:
        observation - state of enviroment following the reset
        """
        observation, info = self.env.reset()
        # Set gripper height
        self.reset_gripper_height()

        self.count = 0
        if jitter:
            for i in range(2):
                self.do_actions(np.random.randint(0,4),np.random.randint(2,4),True)
                

        if self.random_agent is not None:
            for i in range(self.NUM_RND_ACTIONS):
                random_action = self.random_agent.get_action()
                self.step(random_action)
        state = self.get_rope_states()
        normalize_states(state)
        return state

    def render(self):
        self.env.render()

    def end_render(self):
        self.env.close()
