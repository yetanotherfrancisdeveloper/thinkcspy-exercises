# Exercise 9

# Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the
# rectangle. Print a nice message with the answer.

# Ask for width and height of the triangle.
width = float(input("Enter the width of the triangle (in numbers and cm): "))
height = float(input("Enter the height of the triangle (in numbers and cm): "))

# Compute the area
area_rectangle = width * height
# Print the result.
print("The area of the triangle with width of", width, "cm and height of", height, "cm is", area_rectangle, "cm^2.")
