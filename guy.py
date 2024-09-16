import turtle

class Guy(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.speed(0)
        self.penup()
        self.setposition(x, y)
        self.shape("turtle")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color('blue')
    #move object   
    def move_up(self):
        self.setposition(self.xcor(), self.ycor()+20)
    def move_down(self):
        self.sety(self.ycor()-20)
