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

    def reflect_x(self):
        return self.x, - self.y


p = Point(3, 5)
print(p)
print(p.reflect_x())
