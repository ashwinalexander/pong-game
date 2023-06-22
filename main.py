# Create screen
# Create and move paddle
# Create another paddle
# Create the ball and move it
# Detect collision with wall and change trajectory
# Detect collision with paddle and change trajectory
# Detect when paddle misses
# Keep score

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
# Setup the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# turns off animation
screen.tracer(0)


right_paddle = Paddle((360,0))
left_paddle = Paddle((-360,0))
ball = Ball()

screen.update()

screen.listen()
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(.1)
    screen.update()
    ball.move()

    # collision with the upper and lower boundary walls
    if(ball.ycor() >=275 or ball.ycor() <=-275):
        print("coming here")
        ball.y_bounce()

    # collision with the paddles
    if(ball.xcor() > 330 and ball.distance(right_paddle) < 70):
        ball.x_bounce()

        # collision with the paddles
    if (ball.xcor() < -330 and ball.distance(left_paddle) < 70):
        ball.x_bounce()








screen.exitonclick()