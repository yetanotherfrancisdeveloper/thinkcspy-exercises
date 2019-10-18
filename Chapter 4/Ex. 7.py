import turtle
import random

wn = turtle.Screen()
wn.bgcolor("lightyellow")
alex = turtle.Turtle()
alex.shape("turtle")

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for angle in angles:
    alex.forward(100)
    alex.left(angle)

print("The final heading is:", alex.heading())

wn.exitonclick()
