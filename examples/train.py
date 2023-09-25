from stable_baselines3 import PPO
from stable_baselines3 import DQN
import gym
import sys

sys.path.append('./car_custom_gym_env_package')
import car_custom_gym_env

env = gym.make('car-env-custom-v1', render_sim=False, n_steps=1000)

# For Tensorboard logging, add a tensorboard_log argument to the PPO() method
model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=600000)
model.save('model_name')