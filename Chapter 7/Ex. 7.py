# Exercise 7

# Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even
# number and False if it is odd.


def is_even(n):
    """Returns True if n is even and returns False if n is odd"""
    if n % 2 == 0:
        return True
    else:
        return False


print(is_even(11))
