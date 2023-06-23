from turtle import Turtle

BALL_START_POSITION = (0,0)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(BALL_START_POSITION)
        # setting up the coordinate increment (will either be used as a positive
        # or negative value
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .1

    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)

    # key bounce logic: Just change the direction of Y coordinate
    def y_bounce(self):
        self.y_move *= -1

    # key bounce logic: Just change the direction of X coordinate
    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= .9

    def ball_reset(self):
        self.goto(0,0)
        self.move_speed = .1
        self.x_bounce()
