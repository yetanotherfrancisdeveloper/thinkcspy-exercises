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

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        return "The point moved to " + "x = " + str(new_x) + ", y = " + str(new_y)


p = Point(4, 6)
print(p)
movement = p.move(3, 3)
print(movement)
