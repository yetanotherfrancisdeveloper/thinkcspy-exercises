# Exercise 5

# Take the sentence: All work and no play makes Jack a dull boy. Store each word in a separate variable, then print
# out the sentence on one line using print.

# Remember that the name of a variable can't start with a number (just saying).
word1 = 'All'
word2 = 'work'
word3 = 'and'
word4 = 'no'
word5 = 'play'
word6 = 'makes'
word7 = 'Jack'
word8 = 'a'
word9 = 'dull'
word10 = 'boy'

print(word1, word2, word3, word4, word5, word6, word7, word8, word9, word10)

# There are other ways to do this, but I suggest you to see them after having studied strings and lists
# (chapters 9 and 10).

# Using strings:
print(f'{word1} {word2} {word3} {word4} {word5} {word6} {word7} {word8} {word9} {word10}')

# Using lists:
sentence = 'All work and no play makes Jack a dull boy'
words = sentence.split()
re_sentence = ''
for word in range(len(words)):
    # If the word is equal to the last word of the sentence in the list 'words', prints the word without the space at
    # the end. Otherwise, it prints the word with a space at the end (you could make this into a function).
    if words[word] == words[-1]:
        re_sentence += f'{words[word]}'
    else:
        re_sentence += f'{words[word]} '

print(re_sentence)
