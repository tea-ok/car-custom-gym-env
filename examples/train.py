from stable_baselines3 import PPO
import gym
import sys

sys.path.append('./car_custom_gym_env_package')
import car_custom_gym_env

env = gym.make('car-env-custom-v1', render_sim=False, n_steps=1000)
model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=300000)
model.save('agent_300k_timesteps')