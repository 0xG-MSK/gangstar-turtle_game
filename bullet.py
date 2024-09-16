import turtle
import gun


class Bullet(turtle.Turtle):
    def __init__(self, current_position):
        super().__init__()
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.setposition(current_position) #gets the position of the gun here <---
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.2, stretch_wid=0.2)
        self.showturtle()
        