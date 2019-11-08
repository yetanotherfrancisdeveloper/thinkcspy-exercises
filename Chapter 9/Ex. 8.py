def occurrences(text, letter):
    """Removes all the occurrences of a given letter from a given string."""
    removed_occurrences = ""
    for i in text.lower():
        if i != letter:
            removed_occurrences = removed_occurrences + i
    return removed_occurrences


print(occurrences("banana", "a"))
