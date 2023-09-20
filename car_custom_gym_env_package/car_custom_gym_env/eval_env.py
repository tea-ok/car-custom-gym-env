import gym
from gym import spaces
import numpy as np

from time import sleep
import keyboard
import sys

import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

gpio.setup(19, gpio.OUT)
gpio.setup(26, gpio.OUT)

gpio.setup(16, gpio.IN)
gpio.setup(20, gpio.IN)
gpio.setup(21, gpio.IN)

class CarEnv(gym.Env):
    """
    render_sim: (bool) if true, a graphic is generated
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
        else:
            move_forward()
        
        obs=np.array([0, 0, 0])

        if gpio.input(21)==1: obs[0]=1
        if gpio.input(20)==1: obs[1]=1
        if gpio.input(16)==1: obs[2]=1

        reward=-200

        if obs[0] == 1:
            reward += 200
        if obs[1] == 1:
            reward += 1300
            if obs[0] == 0 and obs[2] == 0:
                reward += 800
        if obs[2] == 1:
            reward += 200    

        self.current_time_step += 1
        if self.current_time_step == self.max_time_steps:
            self.done = True

        return obs, reward, self.done, {}

    def render(self, mode='human', close=False):        
        print("Pois päältä...")
        
    def reset(self):
        obs=np.array([0, 0, 0])

        if gpio.input(21)==1: obs[0]=1
        if gpio.input(20)==1: obs[1]=1
        if gpio.input(16)==1: obs[2]=1

        return obs

    def close(self):
        print("Heippa!")

def turn_left(): # vasemmalle Left
    gpio.output(26, 1)
    sleep(0.5)
    gpio.output(26, 0) # = min 10 astetta (arvio)
    print("vas")
    
def turn_right(): #oikealle  Right
    
    gpio.output(19, 1)
    sleep(0.5)
    gpio.output(19, 0) # = plus 10 astetta (arvio)
    print("oik")
    
def move_forward(): #suoraan Direct (Both motors on)
    gpio.output(26, 1)
    gpio.output(19, 1)
    sleep(0.5)
    gpio.output(26, 0)
    gpio.output(19, 0)
    
    print("suor")