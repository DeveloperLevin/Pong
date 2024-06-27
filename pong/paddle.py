from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, corx, cory):
        super().__init__()
        #coordinates of the paddle object
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(5, 1)
        self.goto(corx, cory)

    def up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)