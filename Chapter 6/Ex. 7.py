def sum_to(n):
    """Returns the sum of all integer numbers up to and including n"""
    total_sum = (n * (n + 1)) / 2
    return total_sum


nums_to_sum = int(input("What's the number you want to compute an arithmetic series? "))
print("the sum of the first", nums_to_sum, "integer numbers is", sum_to(nums_to_sum))
