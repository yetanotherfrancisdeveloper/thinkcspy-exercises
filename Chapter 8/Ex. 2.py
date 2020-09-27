# Exercise 2

# Write a function print_triangular_numbers(n) that prints out the first n triangular numbers. A call to print_
# triangular_numbers(5) would produce the following output:
#
# 1       1
# 2       3
# 3       6
# 4       10
# 5       15
#
# (hint: use a web search to find out what a triangular number is.)


def print_triangular_numbers(n):
    """Returns the triangular numbers up to n."""
    for i in range(1, n + 1):
        print(i, "is equal to:", (i * (i + 1)) // 2)


# You could make it so that it doesn't print none (with lists for instance).
print(print_triangular_numbers(5))
