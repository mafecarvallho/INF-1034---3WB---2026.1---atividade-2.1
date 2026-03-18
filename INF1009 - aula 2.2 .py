
import turtle
from turtle import *

t = Turtle()

for _ in range(4): # o underscore ignora a varivael 
    t.fd(100) 
    t.lt(90) #gira em graus

# t.fd(100) - #t.forward() - mesmo comando
# t.lt(90)  -  #t.left()

t.pu() #t.penup - faz a linha para de desenhar ( a caneta n funciona mais)
t.goto(200,300) # mexer a minha turle, com (x,y) - que nem o cartesiano
t.down() # a cantea volta a funcionar

t.color("#8932a8")
t.begin_fill() #coloca no começo pra preecnher
t.fillcolor("Orange") # a cor do fill vai ser diferente da linha 
for _ in range(4): 
    t.fd(100) 
    t.lt(90)
t.end_fill() # só no final pra acbar o preenchimento


#Começo do plano cartesiano

t.pu()
t.goto(0,0)
t.down()
t.forward(300) 
t.stamp # vai ficar uma marca


t.color("Black")
t.begin_fill()
color = textinput("Obter cor" , "digite a cor desejada") # texto vai aparecer
t.fillcolor(color)
t.circle(50)
t.end_fill()

mainloop()
