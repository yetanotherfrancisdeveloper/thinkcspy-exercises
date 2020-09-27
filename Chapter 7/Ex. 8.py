# Exercise 8

# Now write the function is_odd(n) that returns True when n is odd and False otherwise.


def is_odd(n):
    """Returns True if n is odd and returns False if n is even"""
    if n % 2 == 1:
        return True
    else:
        return False


print(is_odd(21))
