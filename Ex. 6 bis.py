def reverse(text):
    txet = ""
    for c in text:
        txet = c + txet

    return txet


print(reverse("Hello"))
