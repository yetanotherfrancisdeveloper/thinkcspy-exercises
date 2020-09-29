# Exercise 18

# Write a function that implements a substitution cipher. In a substitution cipher one letter is substituted for
# another to garble the message. For example A -> Q, B -> T, C -> G etc. your function should take two parameters,
# the message you want to encrypt, and a string that represents the mapping of the 26 letters in the alphabet. Your
# function should return a string that is the encrypted version of the message.


alphabet = "abcdefghijklmnopqrstuxywvz"


def encrypt(message, mapping):
    """Returns an encrypted message."""
    message_lowercase = message.lower()
    map_len = len(mapping)
    encrypted_message = ""
    for i in message_lowercase:
        for j in range(map_len):
            if i == mapping[j]:
                if j == (map_len - 1):
                    encrypted_message = encrypted_message + mapping[j]
                else:
                    encrypted_message = encrypted_message + mapping[j + 1]
    return encrypted_message


print(encrypt("AAA", alphabet))
