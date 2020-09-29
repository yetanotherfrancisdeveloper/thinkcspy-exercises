# Exercise 11

# Sum all the elements in a list up to but not including the first even number.


def sum_up_to_even(a_list):
    """Sums all the numbers in a list up to, but not including, the first even number."""
    sum_to_even = 0
    for i in a_list:
        if i % 2 != 0:
            sum_to_even += i
        elif i % 2 == 0:
            break
    return sum_to_even


print(sum_up_to_even([1, 3, 5, 7, 8, 9, 11]))
