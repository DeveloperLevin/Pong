from turtle import Turtle
import time

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.home()
        self.shapesize(1, 1)
        self.color('white')
        self.penup()
        self.x_move = 2
        self.y_move = 2
        self.move_speed = 0.01

    def move(self):
        cor_x = self.xcor() + self.x_move
        cor_y = self.ycor() + self.y_move
        self.goto(cor_x, cor_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()
            

        