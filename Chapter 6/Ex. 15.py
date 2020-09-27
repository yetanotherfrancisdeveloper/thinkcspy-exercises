# Exercise 15

# Write a function called myPi that will return an approximation of PI (3.14159…). Use the Leibniz approximation.


def my_pi(iterations):
    """This function returns an approximation of pi given the number of iterations."""
    numerator = 1
    denominator = 1
    approx_pi = 0
    for i in range(iterations):
        if i % 2 != 0:
            approx_pi -= numerator/denominator
            denominator += 2
        else:
            approx_pi += numerator/denominator
            denominator += 2
    return approx_pi * 4


print(my_pi(1000))
