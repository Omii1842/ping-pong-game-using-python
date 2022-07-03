from turtle import Turtle
one_positions=[(-185,0),(-185,21),(-185,40),(-185,60)]
sec_positions=[(185,0),(185,21),(185,40),(185,60)]
DOWN=270
UP=90
segments1=[]
segments2=[]


class dd():
    def __init__(self):
         self.create_Dash()
         self.segments1=[]
         self.segments2=[]


    def Dash(self,i):
        t=Turtle()
        t.penup()
        t.shape("square")
        t.color("white")
        t.goto(i)
        segments1.append(t)
        segments2.append(t)
    def create_Dash(self):
        for i in one_positions:
            self.Dash(i)

        for i in sec_positions:
            self.Dash(i)



    def move(self):

        for i in range(len(self.segments1)-1,0,1):
         xcor=self.segments1[i-1].xcor()
         ycor=self.segments2[i-1].ycor()
         self.segments1[i-1].goto(xcor,ycor)
         self.segments1[3].forward(50)


    def up(self):
            self.segments1[3].setheading(90)
