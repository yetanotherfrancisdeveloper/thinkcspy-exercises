# Exercise 9

# Sum up all the negative numbers in a list.


def negative_sum(a_list):
    """Returns the sum of all the negative numbers in a list."""
    total_negatives = 0
    for i in a_list:
        if i < 0:
            total_negatives += i
        else:
            total_negatives += 0
    return total_negatives


print(negative_sum([i for i in range(-5, 5)]))
