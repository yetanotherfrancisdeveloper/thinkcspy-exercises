# Exercise 2


def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] = inventory[fruit] + quantity
    else:
        inventory[fruit] = quantity
    for key in inventory.keys():
        return "The number of " + key + " is " + str(inventory[key])


fruits = {}


print(add_fruit(fruits, "apples", 20))
print(add_fruit(fruits, "apples", 5))
