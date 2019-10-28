def is_right_angled(leg_1, leg_2, hypotenuse):
    """Returns if a triangle is right-angled or not"""
    if hypotenuse ** 2 - (leg_1 ** 2 + leg_2 ** 2) < 0.001:
        return "This is a right triangle"
    else:
        return "This is NOT a right triangle"


print(is_right_angled(3, 3, 4.24))
print(is_right_angled(3, 3, 5))
