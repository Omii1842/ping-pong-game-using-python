from turtle import Turtle,Screen
s=Screen()
t=Turtle()
class score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.hideturtle()
        self.l_score=0
        self.r_score=0

    def l_scor(self,position):
        self.goto(position)
        self.write(self.l_score, align="center", font=("arial", 20, "normal"))

    def r_scor(self, position):
        self.goto(position)
        self.write(self.r_score, align="center", font=("arial", 20, "normal"))
    def l_point(self):
        self.l_score+=1
        self.clear()

    def r_point(self):
        self.r_score+=1
        self.clear()