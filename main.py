from turtle import Turtle,Screen
from Balll import ball
from movements import action
from scorecard import score

import time
mov= ball()
s=Screen()
segments=[]
s.listen()
s.setup(width=400,height=400)
s.bgcolor("Black")
s.title("pong game")
s.tracer(0)
left_p= action((-170, 0))
r_p=action((170, 0))


a=action
sc =score()
game=True
while game:
    s.update()

    mov.mov_ball()




    sc.l_scor((-40,160))
    sc.r_scor((40,160))
    s.onkey(left_p.up, "w")
    s.onkey(left_p.down, "s")


    s.onkey(r_p.up1, "Up")
    s.onkey(r_p.down1, "Down")

    if mov.ycor() > 190 or mov.ycor() < -190:
             mov.bounce_y()



    if mov.distance(left_p) < 50  and mov.xcor() < -155 or mov.distance(r_p) < 50  and mov.xcor()>155 :
       mov.bounce_x()


    if mov.xcor() <  -185 :
        mov.resetpos()
        mov.bounce_x()
        mov.bounce_y()
        sc.r_point()
    if mov.xcor() > 185 :
        mov.resetpos()
        mov.bounce_x()

        sc.l_point()

if mov.distance(left_p) < 50 or mov.distance(r_p) < 50:
    for i in range(100):
        mov.speed(i)






s.exitonclick()
