
rope_xml = """
<mujoco model="rope">
    <compiler angle="radian"/>
    <size njmax="500" nconmax="100"/>
    <worldbody>
        <body name="CB0" pos="-0.2 0 0">
        <inertial pos="0 0 0.01" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
            <geom name="CG0" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
            <body name="CB1" pos="0.04 0 0">
                <inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
                <joint name="CJ0_1" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>
                <joint name="CJ1_1" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>
                <geom name="CG1" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
                <body name="CB2" pos="0.04 0 0">
                    <inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
                    <joint name="CJ0_2" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>
                    <joint name="CJ1_2" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>
                    <geom name="CG2" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
                    <body name="CB3" pos="0.04 0 0">
                        <inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
                        <joint name="CJ0_3" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>
                        <joint name="CJ1_3" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>
                        <geom name="CG3" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
                        <body name="CB4" pos="0.04 0 0">
                            <inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
                            <joint name="CJ0_4" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>
                            <joint name="CJ1_4" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>
                            <geom name="CG4" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
                            <body name="CB5" pos="0.04 0 0">
                                <inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
                                <joint name="CJ0_5" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>
                                <joint name="CJ1_5" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>
                                <geom name="CG5" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
                                <body name="CB6" pos="0.04 0 0">
                                    <inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
                                    <joint name="CJ0_6" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>
                                    <joint name="CJ1_6" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>
                                    <geom name="CG6" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
                                    <body name="CB7" pos="0.04 0 0">
                                        <inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
                                        <joint name="CJ0_7" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>
                                        <joint name="CJ1_7" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>
                                        <geom name="CG7" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
                                        <body name="CB8" pos="0.04 0 0">
                                            <inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
                                            <joint name="CJ0_8" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>
                                            <joint name="CJ1_8" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>
                                            <geom name="CG8" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
                                            <body name="CB9" pos="0.04 0 0">
                                                <inertial pos="0 0 0" quat="0.707107 0 0.707107 0" mass="0.0136136" diaginertia="2.52375e-06 2.52375e-06 6.38791e-07"/>
                                                <joint name="CJ0_9" pos="-0.02 0 0" axis="0 1 0" group="3" damping="0.005"/>
                                                <joint name="CJ1_9" pos="-0.02 0 0" axis="0 0 1" group="3" damping="0.005"/>
                                                <geom name="CG9" size="0.01 0.015" quat="0.707107 0 0.707107 0" type="capsule" rgba="0.8 0.2 0.1 1"/>
                                            </body>
                                        </body>
                                    </body>
                                </body>
                            </body>
                        </body>
                    </body>
                </body>
            </body>
        </body>
    </worldbody>
</mujoco>
"""
