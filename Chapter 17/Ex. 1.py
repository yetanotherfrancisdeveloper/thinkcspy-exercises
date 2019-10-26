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

    def distanceFromPoint(self, target_x, target_y):
        return math.sqrt((target_x - self.x) ** 2 + (target_y - self.y) ** 2)


p1 = Point(3, 3)
p2 = Point(6, 7)
print("P1 : " + str(p1), "P2 : " + str(p2), sep="\n")
print(p1.distanceFromPoint(p2.getX(), p2.getY()))
