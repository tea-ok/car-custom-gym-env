from stable_baselines3 import PPO
from stable_baselines3 import DQN
import gym
import time
import sys
import os

sys.path.insert(0, './car_custom_gym_env_package') # train.py + eval.py
import car_custom_gym_env

continuous_mode = True #if True, after completing one episode the next one will start automatically
random_action = False #if True, the agent will take actions randomly
render_sim = True #if True, a graphic is generated

env = gym.make('car-env-custom-v1', render_sim=render_sim, n_steps=1000)
model = PPO.load("./testing_tensorboard.zip")
model.set_env(env)

random_seed = int(time.time())
model.set_random_seed(random_seed)

obs = env.reset()

# print("Starting program in 30 seconds...")
# time.sleep(30)

try:
    while True:
        if render_sim:
            env.render()

        if random_action:
            action = env.action_space.sample()
        else:
            action, _states = model.predict(obs)

        obs, reward, done, info = env.step(action)

        if done is True:
            print("done")
            if continuous_mode is True:
                state = env.reset()
            else:
                break

finally:
    env.close()
