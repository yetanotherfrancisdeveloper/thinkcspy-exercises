# Exercise 11

# Write a program that will convert degrees celsius to degrees fahrenheit.

# Ask for degrees in celsius.
degrees_celsius = float(input("Write the degrees in celsius (°C) you want converted in degrees fahrenheit (°F): "))
# Compute the equivalent in fahrenheit.
celsius_to_fahrenheit = round((degrees_celsius * 1.8) + 32, 1)
# Print the result.
print(degrees_celsius, "°C (degrees celsius) are equal to", celsius_to_fahrenheit, "°F (degrees fahrenheit).")
