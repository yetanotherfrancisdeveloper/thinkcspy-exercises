import math


def area_of_circle(r):
    """Returns the area of the circle given a certain radius"""
    area = math.pi * r ** 2
    return area


radius = int(input("What is the length of the radius of the circle you want the area to be computed? "))
print("The area of the circle with radius", radius, "is equal to",  area_of_circle(radius))
