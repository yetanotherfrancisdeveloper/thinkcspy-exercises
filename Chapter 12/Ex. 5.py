# Exercise 5

# Write a program that asks the user for a sentence in English and then translates that sentence to Pirate.


english_to_pirate = {"sir": "matey", "hotel": "fleabag inn", "student": "swabbie",
                     "boy": "matey", "madam": "proud beauty"}

english_sentence = input("Enter a sentence in English (without punctuation): ")
english_sentence_words = english_sentence.split()


def translator():
    translated_sentence = []
    for word in english_sentence_words:
        if word in english_to_pirate:
            translated_sentence.append(english_to_pirate[word])
        else:
            translated_sentence.append(word)
    return " ".join(translated_sentence)


print(translator())
