
import turtle
from turtle import *

t= Turtle()

#plano cartesinano
t.goto(0,0)
t.forward(300)
t.stamp()
t.pu()
t.goto(0,0)
t.left(90)
t.down()
t.forward(300)
t.stamp()
t.pu()
t.goto(0,0)
t.left(180)
t.down()
t.forward(300)
t.stamp()
t.pu()
t.goto(0,0)
t.right(90)
t.down()
t.forward(300)
t.stamp()


#Figuras geometricas

t.pu()
t.goto(150 , 150)
t.down()
t.begin_fill()
t.fillcolor("red")
for _ in range (3):
    t.forward(100)
    t.right(120)
t.end_fill()


t.pu()
t.goto(- 150 , 150)
t.down()
t.begin_fill()
t.fillcolor("red")
for _ in range(5):
    t.forward(100)
    t.right(72)

t.end_fill()





mainloop()