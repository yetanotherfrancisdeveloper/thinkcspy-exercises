# Exercise 7

# Write a Python program that assigns the principal amount of 10000 to variable P, assign to n the value 12, and assign
# to r the interest rate of 8% (0.08). Then have the program prompt the user for the number of years, t, that the money
# will be compounded for. Calculate and print the final amount after t years.

# This program allows you to compute the final amount (called Future Value)
# you will have after t years of compound interest on an initial investment P (just a little bit more of info).

P = 10000    # Initial investment.
n = 12       # Number of times the interest is compounded per year.
r = 0.08     # Annual nominal interest rate.

# Ask for the number of years (must be an integer).
t = int(input("For how many years will your investment be compounded for? "))
# Formula to compute the future value.
future_value = P * (1 + r/n) ** (n*t)
# Print the result.
print("The Future Value of your investment after", t, "years will be:", future_value)
