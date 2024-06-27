from turtle import Turtle

class Score(Turtle):
    def __init__(self, corx, cory):
        super().__init__()
        #adds labels to the top of the page that displays scores and high score
        self.score = 0
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(corx, cory)
        self.dis()

    def dis(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Times new Roman", 40, "bold"))
        self.score += 1

        
        
        
        
    