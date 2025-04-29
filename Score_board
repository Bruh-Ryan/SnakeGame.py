from turtle import Turtle
import random
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,280)
        self.score=0
        self.color("white")
        self.hideturtle()
        
    
        
    def score_update(self):
        
        self.write(f"Socre:{self.score}",align="left",font=("Arial",10,"normal"))

    def addPoint(self):
        self.score=self.score+1
        if self.score%5==0:
            self.score=self.score+5
            
        self.clear()
        self.score_update()
    


    def game_pause(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="Center",font=("Arial",20,"normal"))

    def resetscr(self):
        self.score=0
        self.goto(0,280)
        
        
        
        
