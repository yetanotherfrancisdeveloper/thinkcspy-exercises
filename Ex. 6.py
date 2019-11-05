def reverse(text):
    """Returns the reverse of its string argument."""
    reverse_text = ""
    for i in range(len(text) - 1, - 1, - 1):
        reverse_text = reverse_text + text[i]
    return reverse_text


print(reverse("main"))
