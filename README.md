# Custom OpenAI Gym Environment

This is a custom OpenAI gym environment designed for the Future IoT course at Jyväskylä University of Applied Sciences.

## Installation

To install this environment, clone the repository and do the following:

1. Navigate to the root folder with Anaconda Promt (Windows) or Terminal (MacOS/Linux) - this is the folder that contains the `requirements.txt` file.
2. Create a new conda environment with `conda create --name <env_name> python=3.9.2`
3. Activate the environment with `conda activate <env_name>`
4. Run the command `pip install setuptools==65.5.0 pip==21`
    - You might get an error that you need to run a different command to modify pip, simply copy the command that is given to you and run it.
5. Install the other required packages with `pip install -r requirements.txt`

## Usage

To use the environment, you can import it into your own projects as shown in the [examples](./examples/). You can also modify the files in the [examples](./examples/) folder to suit your needs.

An important thing to remember is that you must always check the [init](./car_custom_gym_env_package/car_custom_gym_env/__init__.py) file and uncomment the use case you want to use. For example, if you want to train your model you must uncomment the line:

```python
from car_custom_gym_env.train_env import *
```

And leave the other two imports commented out.

**Note: If using the examples, please ensure that you are running them from the root folder. Do not navigate to the examples folder and run `python train.py` from there. Run `python ./examples/train.py` from theroot folder in stead. If using a code editor such as VS Code, simply check the terminal to see where the Python interpreter is running the code from if you see any `module not found` errors.**

### Example

#### Training and testing a model on your own computer

After installing everything according to the instructions above:

1. Open up the code in your favorite editor from the root folder, in this example we will use VS Code. The view in the explorer should have the following folders and files:
    - .vscode
    - car_custom_gym_env_package
    - examples
    - .gitignore
    - assa2.gif
    - README.md
    - requirements.txt
2. Ensure that you have the correct Python interpreter selected, you can do this by pressing `Ctrl + Shift + P` and typing `Python: Select Interpreter` and selecting the correct one from the list - it should be the Anaconda environment you created earlier.
3. Navigate to the [init](./car_custom_gym_env_package/car_custom_gym_env/__init__.py) file and uncomment the line:

```python
from car_custom_gym_env.train_env import *
```

4. Run the [train.py](./examples/train.py) file by pressing the play button in the top right corner of VS Code, if all is done correctly you will see the car start moving around in the environment, trying to learn how to drive. The training will take a while if you have `total_timesteps` set to a large number, so be patient.
5. After the training is done, a new .zip folder will be created in the root folder, this is the model that was trained. You can now test the model by uncommenting the following line from the [init](./car_custom_gym_env_package/car_custom_gym_env/__init__.py) file:

```python
from car_custom_gym_env.eval_graphic import *
```

Next, run the [eval.py](./examples/eval.py) file by pressing the play button of that file in the top right corner of VS Code. You should see the car driving around in the environment, this time it is using the model that was trained earlier. Ensure that it's loading the correct model by checking the following line in the [eval.py](./examples/eval.py) file:

```python
model = PPO.load("./model_name.zip")
```

6. When testing it on the Raspberry Pi, you can simply copy the model's .zip file to the Raspberry Pi and run the [eval.py](./examples/eval.py) file there, and uncomment the appropriate line in [init](./car_custom_gym_env_package/car_custom_gym_env/__init__.py). Ensure that you have the an Anaconda env on the Raspberry Pi created in the same way as on your own computer and that you have the correct packages installed. You can install the packages in the same way as before, but make sure to also install `RPi.GPIO` (tested using version 0.7.0).

**Common issues/helpful links:**

-   Installing Anaconda: [Link](https://docs.anaconda.com/free/anaconda/install/index.html)
-   Stable Baselines3 v1.4.0 documentation: [Link](https://stable-baselines3.readthedocs.io/en/v1.4.0/)
-   Problems with installation of `gym==0.19.0`: [Link](https://github.com/openai/gym/issues/3176)
