# Exercise 6

# Write a function findHypot. The function will be given the length of two sides of a right-angled triangle and it
# should return the length of the hypotenuse. (Hint: x ** 0.5 will return the square root, or use sqrt from the
# math module)


import math


def find_hypotenuse(cateto_1, cateto_2):
    """Given two legs, returns the hypotenuse"""
    hypotenuse = math.sqrt(cateto_1 ** 2 + cateto_2 ** 2)
    return "The hypotenuse for the sides " + str(cateto_1) + " and " + str(cateto_2) + " is equal to " + str(hypotenuse)


print(find_hypotenuse(3, 5))
