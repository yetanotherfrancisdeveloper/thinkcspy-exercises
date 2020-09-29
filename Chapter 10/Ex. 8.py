# Exercise 8

# Sum up all the even numbers in a list.


def sum_even(a_list):
    """Returns the sum of all the even numbers in a list."""
    total_even = 0
    for i in a_list:
        if i % 2 == 0:
            total_even += i
        else:
            total_even += 0
    return total_even


print(sum_even([i for i in range(10)]))
