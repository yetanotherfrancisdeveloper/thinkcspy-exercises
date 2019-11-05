def print_triangular_numbers(n):
    """Returns the triangular numbers up to n."""
    for i in range(1, n + 1):
        print(i, "is equal to:", (i * (i + 1)) // 2)


print(print_triangular_numbers(5))
