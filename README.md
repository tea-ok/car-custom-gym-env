# Custom OpenAI Gym Environment

This is a custom OpenAI gym environment designed for the Future IoT course at Jyväskylä University of Applied Sciences. 

## Installation

To install this environment, clone the repository and do the following:

1. Navigate to the `car_custom_gym_environment` folder with Anaconda Promt (Windows) or Terminal (MacOS/Linux)
2. Create a new conda environment with `conda create --name <env_name> python=3.9.2`
3. Activate the environment with `conda activate <env_name>`
4. Install the required packages with `pip install -r requirements.txt`


## Usage

To use the environment, you can import it into your own projects as shown in the [examples](./examples/). You can also modify the files in the [examples](./examples/) folder to suit your needs.

An important thing to remember is that you must always check the [init](./car_custom_gym_env_package/car_custom_gym_env/__init__.py) file and uncomment the use case you want to use. For example, if you want to train your model you must uncomment the line:
    
```python
from car_custom_gym_env.train_env import *
```
And leave the other two imports commented out.

**Note: If using the examples, please ensure that you are running them from the `car_custom_gym_environment` folder. Do not navigate to the examples folder and `python train.py` from there. Run `python ./examples/train.py` from the `car_custom_gym_environment` folder in stead. If using a code editor such as VS Code, simply check the terminal to see where the Python interpreter is running the code from if you see any `module not found` errors.**
