# This program converts degrees Celsius (°C) to degrees Fahrenheit (°F).

degreesCelsius = float(input("Write the degrees in Celsius (°C) you want converted in degrees Fahrenheit (°F): "))
CelsiusToFahrenheit = round((degreesCelsius * 1.8) + 32, 1)

print("\n", degreesCelsius, "°C (degrees Celsius) are equal to", CelsiusToFahrenheit, "°F (degrees Fahrenheit).")
