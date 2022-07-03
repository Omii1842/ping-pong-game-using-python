from turtle import Turtle,Screen
import time
class ball(Turtle):
   def __init__(self):
        super().__init__()
        self.make_ball()
        self.x_corr=5
        self.y_corr=5

   def make_ball(self):
       self.shape("circle")
       self.shapesize(1, 1)
       self.goto(0, 0)
       self.color("white")

   def mov_ball(self):
       self.penup()
       x_cor=self.xcor()+self.x_corr
       y_cor=self.ycor()+self.y_corr
       time.sleep(0.06)
       self.goto(x_cor,y_cor)


   def bounce_y(self):
      self.y_corr *=-1



   def bounce_x(self):
        self.x_corr *=-1


   def resetpos(self):
       self.goto(0,0)