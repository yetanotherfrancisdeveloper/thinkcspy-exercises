def count_word_up_to(a_list):
    """Returns how many words occur in a list up to and including the word 'sam'."""
    words_count = 0
    for i in a_list:
        if i.lower() != "sam":
            words_count += 1
        elif i.lower() == "sam":
            words_count += 1
            break
    return words_count


print(count_word_up_to(["James", "Harry", "Hermione", "Sam", "Ron", "Albus", "Severus"]))
