# Exercise 12

# Write a program that will convert degrees fahrenheit to degrees celsius.

# Ask for degrees in fahrenheit.
degrees_fahrenheit = float(input("Write the degrees in Fahrenheit (°F) you want converted in degrees Celsius (°C): "))
# Compute the equivalent in celsius
fahrenheit_to_celsius = round((degrees_fahrenheit - 32) / 1.8, 1)
# Print the result.
print(degrees_fahrenheit, "°F (degrees Fahrenheit) are equal to", fahrenheit_to_celsius, "°C (degrees Celsius).")
