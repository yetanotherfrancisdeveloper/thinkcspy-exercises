import string


Alice_Wonderland = open("/Users/Franc/Desktop/Data Science/txtfiles/studentdata.txt", "r")

words_in_Alice = {}
for line in Alice_Wonderland:
    Alice_line = line.split()
    for i in Alice_line:
        i.translate(str.maketrans(' ', ' ', string.punctuation))
        i = i.lower()
        if i in words_in_Alice:
            words_in_Alice[i] += 1
        else:
            words_in_Alice[i] = 1

words_in_Alice_keys = words_in_Alice.keys()
words_in_Alice_list = list(words_in_Alice.keys())
words_in_Alice_list.sort()
print("The number of 'Alice' is", words_in_Alice["get"])

out = open("alice_words.txt", "w")

for word in words_in_Alice_keys:
    out.write(word + " " + str(words_in_Alice[word]))
    out.write('\n')
