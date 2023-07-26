from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.scoreboard()


    def scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_lscore(self):
        self.l_score =+1
        self.clear()
        self.scoreboard()

    def update_rscore(self):
        self.r_score =+1
        self.clear()
        self.scoreboard()





