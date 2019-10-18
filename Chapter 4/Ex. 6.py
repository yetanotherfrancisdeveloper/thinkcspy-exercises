import turtle

polygon_sides = [int(input("Please enter the number of sides of the polygon "
                           "you want the turtle to draw: (as a number) "))]
length_side = int(input("Enter the length of the side: (as a number) "))
color_side = input("Which color do you want the pen to be? ")
fill_polygon = input("With which color do you want to fill the polygon? ")

wn = turtle.Screen()
wn.bgcolor("lightyellow")
alex = turtle.Turtle()
alex.shape("turtle")

alex.begin_fill()

for i in range(polygon_sides[0]):
    alex.color(color_side, fill_polygon)
    alex.forward(length_side)
    alex.left(180 - (180 * (polygon_sides[0] - 2)) // polygon_sides[0])

alex.end_fill()

wn.exitonclick()
