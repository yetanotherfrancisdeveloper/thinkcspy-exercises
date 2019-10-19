import math

x = int(input("Enter the length of the first cathetus in cm: "))
y = int(input("Enter the length of the second cathetus in cm: "))

hypotenus = math.hypot(x, y)
print("The length of the hypotenus is equal to", hypotenus, "cm.")
