def sum_of_squares(xs):
    """Returns the sum of squares of a list."""
    total_squares = 0
    for i in xs:
        total_squares += i ** 2
    return total_squares


print(sum_of_squares([2, 3, 4]))
