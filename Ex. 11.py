def is_right_angled(x, y, z):
    """Returns if a triangle is right-angled or not"""
    if x > y and x > z:
        return x ** 2 - (y ** 2 + z ** 2) < 0.001
    elif y > x and y > z:
        return y ** 2 - (x ** 2 + z ** 2) < 0.001
    elif z > x and z > y:
        return z ** 2 - (x ** 2 + y ** 2) < 0.001
    else:
        return False


print(is_right_angled(4.24, 3, 3))
print(is_right_angled(3, 4.24, 3))
print(is_right_angled(3, 3, 4.24))
print(is_right_angled(3, 3, 5))
