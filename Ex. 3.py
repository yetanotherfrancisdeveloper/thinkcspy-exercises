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
