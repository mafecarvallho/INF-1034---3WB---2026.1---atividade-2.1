
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
color = textinput("Obter cor" , "digite a cor desejada" )
t.fillcolor(color)
for _ in range (3):
    t.forward(100)
    t.right(120)
t.end_fill()


t.pu()
t.goto(- 150 , 150)
t.down()
t.begin_fill()
color = textinput("Obter cor" , "digite a cor desejada" )
t.fillcolor(color)

for _ in range(5):
    t.forward(100)
    t.right(72)

t.end_fill()

t.pu()
t.goto(- 150 , -250)
t.down()
t.begin_fill()
color = textinput("Obter cor" , "digite a cor desejada" )
t.fillcolor(color)


for _ in range(6):
    t.forward(100)
    t.right(60)

t.end_fill()

t.pu()
t.goto( 250 , - 100)
t.down()
t.begin_fill()
color = textinput("Obter cor" , "digite a cor desejada" )
t.fillcolor(color)

for _ in range(8):
    t.forward(100)
    t.left(45)

t.end_fill()

t.speed(0) 

t.pu()
t.goto( 250 , - 150)
t.down() 

for i in range(50):
    t.forward(i * 2)  
    t.right(45)      

turtle.done()



mainloop()