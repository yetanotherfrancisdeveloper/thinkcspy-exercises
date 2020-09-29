# Exercise 6

# Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example,
# sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:


def sum_of_squares(xs):
    """Returns the sum of squares of a list."""
    total_squares = 0
    for i in xs:
        total_squares += i ** 2
    return total_squares


print(sum_of_squares([2, 3, 4]))
