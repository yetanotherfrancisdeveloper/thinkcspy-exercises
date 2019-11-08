def non_overlap(text, sub):
    """Returns the number of times a given substring repeats itself in a given string."""
    occurrences = 0
    len_sub = len(sub)
    i = 0
    while i <= len(text) - len_sub:
        if sub in text[i: len_sub + i]:
            occurrences = occurrences + 1
            i += len_sub
        else:
            i = i + 1
    return occurrences


print(non_overlap("aaaa", "aa"))
