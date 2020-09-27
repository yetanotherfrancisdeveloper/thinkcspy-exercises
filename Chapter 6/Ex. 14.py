# Exercise 14

# Write a function called mySqrt that will approximate the square root of a number, call it n, by using Newton’s
# algorithm. Newton’s approach is an iterative guessing algorithm where the initial guess is n/2 and each subsequent
# guess is computed using the formula: newguess = (1/2) * (oldguess + (n/oldguess)).


def my_sqrt(n, iterations):
    """This function approximates the square root of a number by using Newton's algorithm.
    It takes as parameters the number you want the square root of and the number of iterations
    you want the algorithm to perform."""
    old_guess = n/2
    for counter in range(iterations):
        new_guess = (1/2) * (old_guess + (n/old_guess))
        old_guess = new_guess
    return new_guess


number = int(input("Enter an integer: "))
iterations_number = int(input("Enter the number of iterations for the algorithm: "))
print(my_sqrt(number, iterations_number))
