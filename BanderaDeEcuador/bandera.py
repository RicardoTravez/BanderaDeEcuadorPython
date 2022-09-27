import turtle
import os
import random

rt = turtle.Screen()
rt.bgcolor('silver')
rt.title('Made in Ecuador')
rt_turtle = turtle.Turtle()
rt_turtle.speed(5)

# PARTES/SECCIONES DE LA BANDERA
def blue_rectangle_below():
    rt_turtle.color('red')
    rt_turtle.begin_fill()
    rt_turtle.forward(300)
    rt_turtle.right(90)
    rt_turtle.forward(120)
    rt_turtle.right(90)
    rt_turtle.forward(600)
    rt_turtle.right(90)
    rt_turtle.forward(120)
    rt_turtle.right(90)
    rt_turtle.forward(300)
    rt_turtle.end_fill()
def white_rectangle():
    rt_turtle.color('blue')
    rt_turtle.begin_fill()
    rt_turtle.left(90)
    rt_turtle.forward(100) 
    rt_turtle.left(90)
    rt_turtle.forward(600)
    rt_turtle.left(90)
    rt_turtle.forward(100) 
    rt_turtle.left(90)
    rt_turtle.forward(300)
    rt_turtle.end_fill()
def blue_rectangle_above():
    rt_turtle.color('yellow')
    rt_turtle.begin_fill()
    rt_turtle.forward(120)
    rt_turtle.left(90)
    rt_turtle.forward(600) 
    rt_turtle.left(90)
    rt_turtle.forward(120)
    rt_turtle.left(90)
    rt_turtle.forward(600)
    rt_turtle.end_fill()
def outline():
    rt_turtle.pensize(10)
    rt_turtle.color('White')
    rt_turtle.shapesize(5)
    rt_turtle.right(90)
    rt_turtle.forward(220)
    rt_turtle.right(90)
    rt_turtle.forward(600)
    rt_turtle.right(90)
    rt_turtle.forward(340)
    rt_turtle.right(90)
    rt_turtle.forward(600)
    rt_turtle.right(90)
    rt_turtle.forward(120)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

escudo = resource_path("escudo.gif")

rt.addshape(escudo)

def letras():
    rt_turtle.color('black')
    rt_turtle.write('Ecuador en la casa', align='center', font=(None, 20, 'bold'))
        
#Zona de ejecucion
blue_rectangle_below()
rt_turtle.forward(300)
white_rectangle()
rt_turtle.forward(300)
rt_turtle.left(90)
rt_turtle.forward(100)
blue_rectangle_above()
outline()

rt_turtle.penup()
image = turtle.Turtle()
image.shape(escudo)
image.goto(-5,50)
outline()

rt_turtle.penup()
rt_turtle.goto(0,-170)
letras()
rt_turtle.goto(-5,-400)
rt.mainloop()
