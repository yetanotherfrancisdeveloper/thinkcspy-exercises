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
