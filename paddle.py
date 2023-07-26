from turtle import Turtle

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []

    def create_paddle(self, x_coordinate):
        self.speed("fastest")
        self.goto(x= x_coordinate, y=0)
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len=1)

    def go_up(self):
        y_new = self.ycor() + 20
        self.goto(self.xcor(), y_new)

    def go_down(self):
        y_new = self.ycor() - 20
        self.goto(self.xcor(), y_new)











