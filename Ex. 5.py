import turtle

wn = turtle.Screen()
wn.bgcolor("lightyellow")
alex = turtle.Turtle()
alex.shape("turtle")

triangle_sides = 3
square_sides = 4
hexagon_sides = 6
octagon_sides = 8

for sides in range(3):
    alex.forward(60)
    alex.left(180 - (180 * (triangle_sides - 2) // triangle_sides))

for sides in range(4):
    alex.forward(60)
    alex.left(180 - (180 * (square_sides - 2) // square_sides))

for sides in range(6):
    alex.forward(60)
    alex.left(180 - (180 * (hexagon_sides - 2) // hexagon_sides))

for sides in range(8):
    alex.forward(60)
    alex.left(180 - (180 * (octagon_sides - 2) // octagon_sides))

wn.exitonclick()
