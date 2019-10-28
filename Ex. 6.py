import math


def findHypot(cateto_1, cateto_2):
    """Given two legs, returns the hypotenuse"""
    hypotenuse = math.sqrt(cateto_1 ** 2 + cateto_2 ** 2)
    return "The hypotenuse for the sides " + str(cateto_1) + " and " + str(cateto_2) + " is equal to " + str(hypotenuse)


print(findHypot(3, 5))
