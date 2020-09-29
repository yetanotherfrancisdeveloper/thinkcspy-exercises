# Exercise 10

# Count how many words in a list have length 5.


def length_5(a_list):
    """Returns how many words in a list have length equal to 5."""
    words_of_five = 0
    for i in a_list:
        if len(i) == 5:
            words_of_five += 1
        else:
            words_of_five += 0
    return words_of_five


print(length_5(["hello", "mom", "party", "cheese", "chocolate"]))
