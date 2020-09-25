# Exercise 8

# Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message
# back to the user with the answer.

import math


# Ask for the radius. This time it can be a float.
radius = float(input("Enter the radius in order to compute the area of your circle: "))
# Compute the area of the circle.
circle_area = round(math.pi * radius, 2)
# Print the result.
print("And the area for your specific circle is:", circle_area, "\n\nThank you for using this program! Bye!")
