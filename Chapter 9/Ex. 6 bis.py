# Exercise 6 (alternative)


def reverse(text):
    """Returns a given string reversed."""
    txet = ""
    for c in text:
        txet = c + txet

    return txet


print(reverse("Hello"))
