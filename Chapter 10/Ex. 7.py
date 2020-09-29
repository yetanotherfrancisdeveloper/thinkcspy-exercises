# Exercise 7

# Write a function to count how many odd numbers are in a list.


def odd_count(a_list):
    """Returns how many odd numbers there are in a list."""
    total_odds = 0
    for i in a_list:
        if i % 2 != 0:
            total_odds += 1
        else:
            total_odds += 0
    return total_odds


print(odd_count([i for i in range(10)]))
