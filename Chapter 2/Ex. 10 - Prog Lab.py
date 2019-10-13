# This program lets you compute KPL for a car and converts it into MPG,
# by asking for kilometers driven and litres used to the user.
# MPG = Miles Per Gallon, KPL = Kilometers Per Litre.

kmDriven = float(input("What's the number of kilometers you have driven? "))
litresUsed = float(input("What's the number of litres you used for this distance? "))

KPL = round(kmDriven / litresUsed, 2)
MPG = round(0.425 * KPL, 2)
print("\nYour car runs", KPL, "Kilometers per Litres, that in Miles per Gallons is", MPG, ".")
