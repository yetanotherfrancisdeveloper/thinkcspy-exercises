# This program creates randomly triangles, squares, hexagons and octagons with random colored sides, random sizes and random positions
# on the screen. I think it can be improved further, but at the moment I don't know how.


import turtle
import random

wn = turtle.Screen()
wn.bgcolor("lightyellow")
wn.colormode(255)
alex = turtle.Turtle()
alex.shape("turtle")


def polygons(t, sides):
    for side in range(sides):
        t.color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
        t.stamp()
        t.forward(30)
        t.left(180 - (180 * (sides - 2) // sides))


polygons_sides = [3, 4, 6, 8]
for i in range(30):
    alex.up()
    alex.setpos(float(random.randrange(-200, 200)), float(random.randrange(-200, 200)))
    alex.down()
    alex.pensize(random.randrange(2, 10))
    polygons(alex, random.choice(polygons_sides))

wn.exitonclick()
