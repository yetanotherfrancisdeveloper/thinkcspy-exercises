# Exercise 10

# Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the
# triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return
# True if the triangle is right-angled, or False otherwise.
#
# Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for
# equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up
# as
# if  abs(x - y) < 0.001:      # if x is approximately equal to y
#     ...


def is_right_angled(leg_1, leg_2, hypotenuse):
    """Returns if a triangle is right-angled or not"""
    if hypotenuse ** 2 - (leg_1 ** 2 + leg_2 ** 2) < 0.001:
        return "This is a right triangle"
    else:
        return "This is NOT a right triangle"


print(is_right_angled(3, 3, 4.24))
print(is_right_angled(3, 3, 5))
