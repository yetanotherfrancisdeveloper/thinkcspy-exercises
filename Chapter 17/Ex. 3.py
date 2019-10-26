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

    def slope_from_origin(self):
        origin_x = 0
        origin_y = 0
        return (self.y - origin_y) / (self.x - origin_x)


p = Point(3, 6)
print("The slope for the point", p, "is", p.slope_from_origin())
