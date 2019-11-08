import turtle


def rules(axiom):
    """Rules of the L-system."""
    transformed = ""
    if axiom.upper() == "X":
        transformed += "X+YF++YF-FX--FXFX-YF+"
    elif axiom.upper() == "Y":
        transformed += "-FX+YFYF++YF+FX--FX-Y"
    else:
        transformed = axiom
    return transformed


def process(start_string):
    """Returns the change in the axiom after having applied the rule."""
    pattern = ""
    for char in start_string:
        pattern += rules(char)
    return pattern


def l_system(iterations, axiom):
    """Returns the L-system."""
    start = axiom
    end_string = ""
    for i in range(iterations):
        end_string = process(start)
        start = end_string
    return end_string


def draw_l_system(t, system, angle, distance):
    """Draws the L-system."""
    for char in system:
        if char == "F":
            t.forward(distance)
        elif char == "-":
            t.left(angle)
        elif char == "+":
            t.right(angle)


def main():
    directions = l_system(5, "FX")
    print(directions)

    wn = turtle.Screen()
    wn.bgcolor("lightyellow")
    jack = turtle.Turtle()
    jack.up()
    jack.backward(200)
    jack.down()
    jack.speed(10)
    draw_l_system(jack, directions, 60, 5)

    wn.exitonclick()


main()
