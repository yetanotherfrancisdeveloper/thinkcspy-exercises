same_sentence = []
repeated_sentence = "We like Python's turtles!"

for i in range(100):
    same_sentence.append(repeated_sentence)

print(same_sentence)
print("The sentence has been repeated for:", same_sentence.count(repeated_sentence), "times.")

# To complete the exercise would have been enough to do the following (I think):
print('\n\nThe "easier" way to do the exercise:')
for i in range(100):
    print("We like Python's turtles!")
