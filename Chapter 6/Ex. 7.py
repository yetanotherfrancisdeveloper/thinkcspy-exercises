# Exercise 7

# Write a fruitful function sumTo(n) that returns the sum of all integer numbers up to and including n. So sumTo(10)
# would be 1+2+3...+10 which would return the value 55. Use the equation (n * (n + 1)) / 2.


def sum_to(n):
    """Returns the sum of all integer numbers up to and including n"""
    total_sum = (n * (n + 1)) / 2
    return total_sum


nums_to_sum = int(input("What's the number you want to compute an arithmetic series? "))
print("the sum of the first", nums_to_sum, "integer numbers is", sum_to(nums_to_sum))
