# Exercise 10

# Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number
# of gallons used. Print a nice message with the answer.

# MPG = Miles Per Gallon, KPL = Kilometers Per Litre.

# Ask for kilometers and litres used.
km_driven = float(input("What's the number of kilometers you have driven? "))
litres_used = float(input("What's the number of litres you used for this distance? "))

# Compute the KPL and the MPG. The results are rounded to two decimals (the second parameter of the method).
KPL = round(km_driven / litres_used, 2)
MPG = round(0.425 * KPL, 2)
# Print the result.
print("\nYour car runs", KPL, "Kilometers per Litres, that in Miles per Gallons is", MPG, ".")
