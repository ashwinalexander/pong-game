from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def left_point_increment(self):
        self.left_score += 10
        self.update_score()

    def right_point_increment(self):
        self.right_score += 10
        self.update_score()

    def update_score(self):
        self.clear();
        self.goto(-100, 200)
        self.write(self.left_score, move=False, align="left", font=("Calibri", 20, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, move=False, align="left", font=("Calibri", 20, "normal"))





