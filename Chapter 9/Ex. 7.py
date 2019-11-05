def mirror(text):
    """Returns a string containing the original string and the string backward."""
    mirror_text = text
    for i in range(len(text) - 1, - 1, - 1):
        mirror_text = mirror_text + text[i]
    return mirror_text


print(mirror("main"))
