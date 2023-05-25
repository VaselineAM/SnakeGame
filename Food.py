from turtle import Turtle
import random
class Food:
    def __init__(self):
        self.food = Turtle() #creating an object within a class
        self.food.shape("circle")
        self.food.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food.color('blue')
        self.food.penup()
        self.food.speed(0)
    
    def refresh(self):
        random_x = random.randint(-250,250)
        random_y = random.randint(-250,250)
        self.food.setpos(random_x,random_y)
