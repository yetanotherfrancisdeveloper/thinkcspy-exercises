def is_even(n):
    """Returns True if n is even and returns False if n is odd"""
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    """Returns True if n is odd and returns False if n is even"""
    if is_even(n):
        return False
    if not is_even(n):
        return True


print(is_even(4), is_odd(4), sep='\n')
