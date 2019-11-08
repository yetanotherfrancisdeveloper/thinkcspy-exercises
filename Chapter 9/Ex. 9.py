def mirror_back(text):
    """Returns a string backward."""
    mirror_text = text
    for i in range(len(text) - 1, - 1, - 1):
        mirror_text = mirror_text + text[i]
    len_mirrored = len(mirror_text)
    return mirror_text[len_mirrored // 2:]


def is_mirror(palindrome):
    """Returns if a word is or not a palindrome"""
    if palindrome in mirror_back(palindrome):
        return True
    else:
        return False


def is_mirror_2(pal):
    """Returns if a word is or not a palindrome (using slicing for exercising)."""
    pal_len = len(pal)
    half_pal = len(pal) // 2
    if mirror_back(pal[:half_pal]) in pal[half_pal:]:
        return True
    else:
        if pal[:pal_len] == pal[pal_len + 1:]:
            return True
        else:
            return False


print(is_mirror("radar"))
print(is_mirror("hannah"))
print(is_mirror("house"))
print(is_mirror_2("radar"))
print(is_mirror_2("hannah"))
print(is_mirror_2("house"))
