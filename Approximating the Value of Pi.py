# This program approximates the value of pi by playing a game of darts with a
# dartboard (circle) of area equal to pi and a piece of wood (square) of area equal to 4

import random
import math


def throws_scored(n):
    """Returns the number of times the darts landed within the dartboard"""
    darts_scoring = 0
    center_x = 0
    center_y = 0
    for i in range(n):
        if math.sqrt((center_x - random.uniform(-1, 1)) ** 2 + (center_y - random.uniform(-1, 1)) ** 2) <= 1:
            darts_scoring += 1
    return darts_scoring


def result():
    """Returns the approximation of pi given n throws and tests the result at a given percentage of tolerance"""
    throws = int(input("Enter the number of darts that will be thrown: "))
    approx_pi = throws_scored(throws) / throws * 4
    print(approx_pi)
    tolerance_percent = float(input("Enter the percentage of tolerance for the test: "))
    if (approx_pi - (tolerance_percent * math.pi)) <= approx_pi <= approx_pi + (approx_pi + (tolerance_percent * math.pi)):
        return "Accepted!"
    else:
        return "Failed"


print(result())
