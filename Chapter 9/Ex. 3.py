# Exercise 3

# 


def count_char(text, char):
    """Returns the number of alphabetic characters and the number of times a "character" is in the text."""
    alphabetic_char = 0
    char_count = 0
    for i in text:
        if i != " ":
            alphabetic_char += 1
            if i == char:
                char_count += 1
    char_percentage = ((char_count / alphabetic_char) * 100)
    return "Your text contains " + str(alphabetic_char) + " alphabetic characters, of which " + str(char_count) + " " \
           + "(" + "{0:.2f}".format(char_percentage) + " %)" + " are \"e\"."

    # For rounding to 2 decimals you could have also used this: "\"%.2f\" % char_percentage
    #                                          instead of this: "{0:.2f}".format(char_percentage)


paragraph = """Plants are more courageous than almost all human beings: an orange tree would rather die than 
            produce lemons, whereas instead of dying the average person would rather be someone they are not."""

print(count_char(paragraph, "e"))
