# Exercise 13

# Rewrite the function sumTo(n) that returns the sum of all integer numbers up to and including n. This time use the
# accumulator pattern.


def sum_to(n):
    """Returns the sum of all integer numbers up to and including n using an accumulation pattern"""
    total_sum = 0
    for i in range(1, n + 1):
        total_sum = total_sum + i
    return total_sum


nums_to_sum = int(input("Type the number you want to compute the arithmetic series for: "))
print("The result of the arithmetic series given the number", nums_to_sum, "is", sum_to(nums_to_sum))
