def integer_digits(n):
    """Returns the number of digits of a given integer."""
    n = str(n)
    num_of_digits = 0
    while num_of_digits < len(n):           # Or just use the len() function to determine the length of the integer ...
        num_of_digits += 1
    return "The number of digits for " + n + " is equal to " + str(num_of_digits)


print(integer_digits(8976))
