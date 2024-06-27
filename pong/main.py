from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from score import Score
import time
import winsound

#Set Screen Details
screen = Screen()
screen.bgcolor('Black')
screen.title('Pong')
screen.setup(800, 600)
screen.tracer(0)

#Create paddles
paddle1 = Paddle(370, 0)
paddle2 = Paddle(-370, 0)
#Create a ball object
ball = Ball()
#create a scoreboard for the two players
player1 = Score(-40, 240)
player2 = Score(40, 240)

#function to run the game
def start():
    ball.home()
    game_start = True
    while game_start:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        
        #Detect wall Collision
        if ball.ycor() > 275 or ball.ycor() < -275:
            ball.bounce_y()

        #Collisions with paddle
        if ball.distance(paddle1) < 58 and ball.xcor() == 350 or ball.distance(paddle2) < 58 and ball.xcor() == -350:
            ball.bounce_x()
            winsound.Beep(2000, 100)

        #if ball goes past either paddle
        if ball.xcor() > 370:
            player1.dis()
            ball.reset_position()

        if ball.xcor() < -370:
            player2.dis()
            ball.reset_position()

#functions to move the snake
screen.onkeypress(paddle1.up, 'Up')
screen.onkeypress(paddle1.down, 'Down')
screen.onkeypress(paddle2.up, 'w')
screen.onkeypress(paddle2.down, 's')
screen.onkey(start, "space")

screen.listen()

screen.update()

screen.mainloop()
screen.exitonclick()
