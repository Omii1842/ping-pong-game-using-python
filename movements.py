
from turtle import Turtle
dash=[]
class action(Turtle):
    def __init__(self,position):
      super().__init__()
      self.penup()
      self.shape("square")
      self.shapesize(5, 1)
      self.goto(position)
      self.color("white")
      self.speed(5)

    def up1(self):
        paddle_y = self.ycor() + 20
        self.goto(self.xcor(), paddle_y)

    def down1(self):
            paddle_y = self.ycor() - 20
            self.goto(self.xcor(), paddle_y)

    def up(self):
        paddle_y=self.ycor()+20
        self.goto(self.xcor(),paddle_y)
    def down(self):
        paddle_y = self.ycor() - 20
        self.goto(self.xcor(), paddle_y)

