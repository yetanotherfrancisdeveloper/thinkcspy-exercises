# Exercise 19

# Search on the internet for a way to calculate an approximation for pi. There are many that use simple arithmetic.
# Write a program to compute the approximation and then print that value as well as the value of math.pi from the
# math module.


import math

approx_pi = 22 / 7
print("A common approximation of pi is", approx_pi, "while the math module pi is", math.pi,
      "\nThe difference between the two is equal to", approx_pi - math.pi)
