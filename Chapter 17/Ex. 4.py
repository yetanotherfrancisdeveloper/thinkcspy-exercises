import math


class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    def __str__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def line_equation(self, other_x, other_y):
        m = (other_y - self.y) / (other_x - self.x)
        b = ((other_x * self.y) - (self.x * other_y)) / (other_x - self.x)
        return m, b


p = Point(4, 11)
print(p)
coefficients = p.line_equation(6, 15)
print(coefficients)
print(type(coefficients))
