import turtle

wn = turtle.Screen()
wn.bgcolor("lightyellow")
alex = turtle.Turtle()
alex.left(36)

for i in range(5):
    alex.forward(150)
    alex.left(180 - 36)

wn.exitonclick()
