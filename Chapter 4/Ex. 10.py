# Exercise 10

# Write a program to draw a face of a clock that looks something like this (check the image on the book)


import turtle

wn = turtle.Screen()
wn.bgcolor("lightyellow")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.pensize(3)

for i in range(12):
    alex.up()
    alex.forward(100)
    alex.down()
    alex.forward(10)
    alex.up()
    alex.forward(20)
    alex.stamp()
    alex.setpos(0, 0)
    alex.left(30)

wn.exitonclick()
