import turtle as t
import random

timy = t.Turtle()
t.colormode(255)
def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def draw(z):
    
    for i in range(int(360/z)):
        timy.speed("fastest")
        timy.color(color())
        timy.circle(100)
        a=timy.heading()
        timy.setheading(a+z)
        timy.circle(100)
#main
draw(10)
