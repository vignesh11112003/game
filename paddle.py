from turtle import Turtle
class Paddle(Turtle):

    def __init__(self,cor):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(5, 1)
        self.penup()
        self.goto(cor)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
