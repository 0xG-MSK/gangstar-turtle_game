import turtle
import random as rd

class Ops(turtle.Turtle):
    def __init__(self, pace): #<---
        super().__init__()
        
    #def generate_enemies(self):
        self.speed(0)
        self.penup()
        self.colors = ["red","yellow","orange","green","indigo","violet"]
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.setposition(rd.randint(0, 320), rd.randint(-320, 320))
        #self.setposition(0, 0)
        self.shape("turtle")
        self.color(rd.choice(self.colors))
        self.setheading(180)
        self.pace = pace #gets the position from parameter
        
    def walk(self):
        """moves the enemies due to space"""
        self.fd(self.pace)
        
    def die(self):
        """simulates killing of enemies """
        self.color("white")
        self.setheading(0)
        self.shapesize(stretch_len=0.2, stretch_wid=0.2)
        self.hideturtle()
        self.setposition(660, 350)
        self.color("yellow")
        

        
           