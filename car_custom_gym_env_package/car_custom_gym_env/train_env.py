import gym
from gym import spaces
import numpy as np

from graphics import *
import keyboard
import sys

sys.path.append('./car_custom_gym_env_package/car_custom_gym_env')
from render import *

class CarEnv(gym.Env):
    """
    render_sim: (bool) Unimplemented - simulation is always rendered
    n_steps: (int) number of time steps
    """

    def __init__(self, render_sim=False, n_steps=1000):
        self.render_sim = render_sim
        self.max_time_steps = n_steps      
        self.done = False
        self.current_time_step = 0

        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.MultiBinary(3)
    
    def step(self, action):
        if keyboard.is_pressed('q'):
                sys.exit("Closed by user")

        if action == 0:
            turn_left()
        elif action == 1:
            turn_right()
        elif action == 2:
            move_forward()
        
        draw_car()

        obs = get_obs()

        reward=-200

        if obs[0] == 1:
            reward += 200
        if obs[1] == 1:
            reward += 1300
            if obs[0] == 0 and obs[2] == 0:
                reward += 800
        if obs[2] == 1:
            reward += 200

        center_car()

        self.current_time_step += 1
        if self.current_time_step == self.max_time_steps:
            self.done = True

        return obs, reward, self.done, {}

    def render(self, mode='human', close=False):        
        # Rendering is done in the step function
        pass
        
    def reset(self):
        obs = get_obs()
        return obs

    def close(self):
        # Closing is done in the step function
        pass