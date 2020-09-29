# Exercise 5

# Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum
# value. (Note: there is a builtin function named max but pretend you cannot use it.)


import random

numbers = []
for i in range(0, 100):
    numbers.append(random.randrange(0, 1000))


def list_max(a_list):
    """Returns the max value in a list."""
    a_list.sort()
    return a_list[-1]


print(max(numbers))
print(list_max(numbers))
