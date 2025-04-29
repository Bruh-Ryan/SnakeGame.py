from turtle import Turtle as t
import random

class food(t):
    def __init__(self):
            super().__init__()
            self.shape("circle")
            self.penup()
            self.shapesize(stretch_len=.5,stretch_wid=.5)
            self.color('Red')
            self.speed(0)
            self.refresh()
            
    def refresh(self):
          self.goto(x=random.randint(-280,280),y=random.randint(-280,280))
          

    def Super_food(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.8,stretch_wid=.8)
        self.color('Green')
        self.speed(0)
        self.refresh()
