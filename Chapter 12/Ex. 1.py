import string


def count_all(a_string):
    """Returns the number of times a letter appears in a given string."""
    counts = {}
    for letter in a_string.lower():
        if letter in list(counts.keys()):
            counts[letter] += 1
        elif letter == " ":
            pass
        else:
            counts[letter] = 1
    for k in sorted(counts):
        print(k, counts[k], sep="\t")


sentence = input("Please enter a sentence: ")
count_all(sentence)
