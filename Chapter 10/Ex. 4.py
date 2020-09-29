# Exercise 4

# Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module).
# Write a function called average that will take the list as a parameter and return the average.


import random

numbers = []
for i in range(0, 100):
    numbers.append(random.randrange(0, 1000))


def average(list_of_nums):
    """Returns the average value of a list."""
    sum_of_nums = 0
    for num in list_of_nums:
        sum_of_nums += num
    return sum_of_nums / len(list_of_nums)


print(average(numbers))
