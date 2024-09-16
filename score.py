import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(-330, 300)
        self.score = 0
        
    def show_score(self):
        """write the score of enemies killed"""
        self.write(f"SCORE: {self.score}", font=("Times New Roman", 8, "normal"))
        
    def update_score(self):
        """updates the score board"""
        self.score += 1
        self.clear()
        self.show_score()
       
    def game_over(self):
        """declares when guy object has been killed"""
        self.clear()
        self.setposition(0, 0)
        self.color("red")
        self.write(f"WASTED, don't let the Ops catch you slackin' again.\nSCORE: {self.score}", align="center")