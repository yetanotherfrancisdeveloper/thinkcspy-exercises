# Exercise 13

# Although Python provides us with many list methods, it is good practice and very instructive to think about how they
# are implemented. Implement a Python function that works like the following:
#
# a) count
# b) in
# c) reverse
# d) index
# e) insert


def count(a_list):
    """Returns the number of items in a list."""
    items_number = 0
    i = 0
    while i < len(a_list):
        items_number += 1
        i += 1
    return items_number


def is_in_list(a_list, item):
    """Returns 'True' if an item is in the given list, otherwise returns 'False'."""
    if item in a_list:
        return True
    else:
        return False


def reverse(a_list):
    """Returns the list with its items reversed."""
    a_list = a_list[::-1]
    return a_list


def index(a_list, item):
    """Returns the index of an intem in a list."""
    for i in range(len(a_list)):
        if a_list[i] == item:
            return i
    else:
        return "The item you're looking for is not here."


def insert(a_list, item_index, item):
    """Adds an item into a given list at the desired index."""
    sliced_list = []
    if item_index >= len(a_list):
        a_list = a_list + [item]
    else:
        for i in range(len(a_list)):
            if i == item_index:
                sliced_list += a_list[i:]
                del a_list[i:]
                a_list.append(item)
                for j in sliced_list:
                    a_list.append(j)
    return a_list


print(count([1, 3]))
print(is_in_list([1, 3], 3))
print(reverse([1, 3]))
print(index([1, 3], 3))
print(insert([1, 3], 0, 5))
