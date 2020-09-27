# Exercise 3

# Write a function, is_prime, that takes a single integer argument and returns True when the argument is a prime
# number and False otherwise.


import math


def is_prime(n):
    """Returns True if n is a prime number."""
    for i in range(1, n):
        while i != 1 and i != n:
            if n % i == 0:
                return False
            else:
                return True


print(is_prime(23))
