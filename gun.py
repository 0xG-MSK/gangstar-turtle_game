import turtle
import bullet

class Gun(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.penup()
        self.color("red")
        self.x = x
        self.y = y
        self.setposition(self.x, self.y)
        self.current_position = (x, y) #buffer to hold position of guy object

    def move_up(self):
        """moves the gun up"""
        self.setposition(self.xcor(), self.ycor()+20)
        self.current_position = self.position()
    def move_down(self):
        """moves the gun down"""
        self.sety(self.ycor()-20)
        self.current_position = self.position()
