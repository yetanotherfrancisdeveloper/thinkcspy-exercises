# This program converts degrees Fahrenheit (°F) to degrees Celsius (°C).

degreesFahrenheit = float(input("Write the degrees in Fahrenheit (°F) you want converted in degrees Celsius (°C): "))
FahrenheitToCelsius = round((degreesFahrenheit - 32) / 1.8, 1)

print("\n", degreesFahrenheit, "°F (degrees Fahrenheit) are equal to", FahrenheitToCelsius, "°C (degrees Celsius).")
