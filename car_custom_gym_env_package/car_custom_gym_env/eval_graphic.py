import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
import math
import os

from time import sleep
from graphics import Line, Circle, Point, GraphWin, Image
import keyboard
import sys

# Graphics setup
angle = 75
x2 = 50
y2 = 350

l=Line(Point(0, 0), Point(0, 0))
l2=Line(Point(0, 0), Point(0, 0))
l3=Line(Point(0, 0), Point(0, 0))
l4=Line(Point(0, 0), Point(0, 0))
l5=Line(Point(0, 0), Point(0, 0))
l6=Line(Point(0, 0), Point(0, 0))
l7=Line(Point(0, 0), Point(0, 0))
l8=Line(Point(0, 0), Point(0, 0))

c1=Circle(Point(0, 0), 7)
c2=Circle(Point(0, 0), 7)
c3=Circle(Point(0, 0), 7)

paper = GraphWin(width=800, height=800)
myImage = Image(Point(400,400), 'assa2.gif')
myImage.draw(paper)

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
        
        global x2, y2, angle, myImage
    
        length=50
        length2=50/4
        length3=50*2
    
        rad2=math.cos(math.radians(angle))
        rad=math.sin(math.radians(angle))
        
        draw_car()

        x3=int(x2 + length2*rad2 - length3*rad)
        y3=int(y2 + length2*rad + length3*rad2)
        if x3<1: x3=1
        if x3>799: x3=799
        if y3<1: y3=1
        if y3>799: y3=799
        red, green, blue = myImage.getPixel(x3, y3)
        
        x3=int(x2 - length2*rad2 - length3*rad)
        y3=int(y2 - length2*rad + length3*rad2)
        if x3<1: x3=1
        if x3>799: x3=799
        if y3<1: y3=1
        if y3>799: y3=799
        red2, green2, blue2 = myImage.getPixel(x3, y3)
        
        x3=int(x2 - length3*rad)
        y3=int(y2 + length3*rad2)
        if x3<1: x3=1
        if x3>799: x3=799
        if y3<1: y3=1
        if y3>799: y3=799
        red3, green3, blue3 = myImage.getPixel(x3, y3)

        obs=np.array([0, 0, 0])
        
        if red==0 and green==0 and blue==0: obs[0]=1
        if red2==0 and green2==0 and blue2==0: obs[2]=1
        if red3==0 and green3==0 and blue3==0: obs[1]=1

        reward=-200

        if obs[0] == 1:
            reward += 200
        if obs[1] == 1:
            reward += 1300
            if obs[0] == 0 and obs[2] == 0:
                reward += 800
        if obs[2] == 1:
            reward += 200

        if x2<0:
            x2=800
        if x2>800:
            x2=0
        if y2<0:
            y2=800
        if y2>800:       
            y2=0

        self.current_time_step += 1
        if self.current_time_step == self.max_time_steps:
            self.done = True        

        return obs, reward, self.done, {}

    def render(self, mode='human', close=False):        
        # print("Pois päältä...")
        pass
        
    def reset(self):
        return np.array([0, 0, 0])

    def close(self):
        # print("Heippa!")
        pass

def draw_car():
    length=50
    length2=50/4
    length3=50*2
    global angle, l, l2, l3, l4, l5, l6, x2, y2, c1, c2, c3
 
    rad2=math.cos(math.radians(angle))
    rad=math.sin(math.radians(angle))
   
    l.undraw()
    l2.undraw()
    l3.undraw()
    l4.undraw()
    l6.undraw()
    
    c1.undraw()
    c2.undraw()
    c3.undraw()
    
    l=Line(Point(x2, y2), Point(x2 + length*rad2, y2 + length*rad))
    l2=Line(Point(x2, y2), Point(x2 - length*rad2, y2 - length*rad))
    l3=Line(Point(x2 + length2*rad2, y2 + length2*rad), Point(x2 + length2*rad2 - length3*rad , y2 + length2*rad + length3*rad2))
    l4=Line(Point(x2 - length2*rad2, y2 - length2*rad), Point(x2 - length2*rad2 - length3*rad , y2 - length2*rad + length3*rad2))
    
    l6=Line(Point(x2, y2), Point(x2 - length3*rad, y2 + length3*rad2))
    
    c1=Circle(Point(x2 + length2*rad2 - length3*rad , y2 + length2*rad + length3*rad2), 7).draw(paper)
    c2=Circle(Point(x2 - length2*rad2 - length3*rad, y2 - length2*rad + length3*rad2), 7).draw(paper)
    c3=Circle(Point(x2 - length3*rad, y2 + length3*rad2), 7).draw(paper)
   
    l.draw(paper)
    l2.draw(paper)
    l3.draw(paper)
    l4.draw(paper)
    l6.draw(paper)

def turn_left():
    global angle, x2, y2
    
    length=50
    length2=50/4
    length3=50*2
    
    rad2=math.cos(math.radians(angle))
    rad=math.sin(math.radians(angle))
    
    x4=x2 + length*rad2
    y4=y2 + length*rad
    
    angle=angle-1

    if angle<0:
        angle=360+angle
    elif angle>360:
        angle=angle-360   
        
    if angle<90:
        angle2=angle
        rad2=math.cos(math.radians(angle2))
        rad=math.sin(math.radians(angle2))
        x2=x4 - length*rad2
        y2=y4 - length*rad
    elif angle>=90 and angle<180:
        angle2=90-(angle-90)
        rad2=math.cos(math.radians(angle2))
        rad=math.sin(math.radians(angle2))
        x2=x4 + length*rad2
        y2=y4 - length*rad
    elif angle>=180 and angle<270:
        angle2=270-angle
        rad2=math.cos(math.radians(angle2))
        rad=math.sin(math.radians(angle2))
        x2=x4 + length*rad
        y2=y4 + length*rad2
    elif angle>=270:
        angle2=360-angle
        rad2=math.cos(math.radians(angle2))
        rad=math.sin(math.radians(angle2))
        x2=x4 - length*rad2
        y2=y4 + length*rad
        
    angle=angle-1

    if angle<0:
        angle=360+angle
    elif angle>360:
        angle=angle-360
    
def turn_right():
    global angle, x2, y2
    
    length=50
    length2=50/4
    length3=50*2
    
    rad2=math.cos(math.radians(angle))
    rad=math.sin(math.radians(angle))
    
    x4=x2 - length*rad2
    y4=y2 - length*rad
    
    angle=angle+1

    if angle<0:
        angle=360+angle
    elif angle>360:
        angle=angle-360   
        
    if angle<90:
        angle2=angle
        rad2=math.cos(math.radians(angle2))
        rad=math.sin(math.radians(angle2))
        x2=x4 + length*rad2
        y2=y4 + length*rad
    elif angle>=90 and angle<180:
        angle2=90-(angle-90)
        rad2=math.cos(math.radians(angle2))
        rad=math.sin(math.radians(angle2))
        x2=x4 - length*rad2
        y2=y4 + length*rad
    elif angle>=180 and angle<270:
        angle2=270-angle
        rad2=math.cos(math.radians(angle2))
        rad=math.sin(math.radians(angle2))
        x2=x4 - length*rad
        y2=y4 - length*rad2
    elif angle>=270:
        angle2=360-angle
        rad2=math.cos(math.radians(angle2))
        rad=math.sin(math.radians(angle2))
        x2=x4 + length*rad2
        y2=y4 - length*rad
        
    angle=angle+1

    if angle<0:
        angle=360+angle
    elif angle>360:
        angle=angle-360
    
def move_forward():
    global angle, x2, y2
    
    length=50 / 5
    length2=50/4
    length3=50*2
    
    rad2=math.cos(math.radians(angle))
    rad=math.sin(math.radians(angle))
    
    x2=x2 - length*rad
    y2=y2 + length*rad2