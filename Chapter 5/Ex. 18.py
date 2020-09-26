# Exercise 18

# The Pythagorean Theorem tells us that the length of the hypotenuse of a right triangle is related to the lengths
# of the other two sides. Look through the math module and see if you can find a function that will compute this
# relationship for you. Once you find it, write a short program to try it out.


import math

x = int(input("Enter the length of the first cathetus in cm: "))
y = int(input("Enter the length of the second cathetus in cm: "))

hypotenuse = math.hypot(x, y)
print("The length of the hypotenuse is equal to", hypotenuse, "cm.")
