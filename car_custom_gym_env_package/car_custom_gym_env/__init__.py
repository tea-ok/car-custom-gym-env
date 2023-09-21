# Uncomment below line for training, comment other import
#from car_custom_gym_env.train_env import *

# Uncomment below line for evaluation with car, comment other import
#from car_custom_gym_env.eval_env import *

# Uncomment below line for evaluation with graphics, comment other import
from car_custom_gym_env.eval_graphic import *
from gym.envs.registration import register

register(
    id='car-env-custom-v1',
    entry_point='car_custom_gym_env:CarEnv',
    kwargs={'render_sim': False, 'n_steps': 1000}
)
