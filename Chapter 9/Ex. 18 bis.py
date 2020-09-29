# Exercise 18 (alternative)


alphabet = "abcdefghijklmnopqrstuxywvz"


def cipher(elements):
    """Returns a code to cipher a message"""
    encrypted_alphabet = ""
    for i in range(len(elements) - 1):
        if i % 2 == 0 and i % 3 == 0:
            encrypted_alphabet = encrypted_alphabet + "|"
        elif i % 2 == 0:
            encrypted_alphabet = encrypted_alphabet + "."
        elif i % 3 == 0:
            encrypted_alphabet = encrypted_alphabet + "-"
        else:
            encrypted_alphabet = encrypted_alphabet + "_"
    return encrypted_alphabet


def encrypt(message, mapping):
    """Returns an encrypted message."""
    map_encrypted = cipher(mapping)
    message_lowercase = message.lower()
    map_len = len(mapping)
    encrypted_message = ""
    for i in message_lowercase:
        for j in range(map_len):
            if i == mapping[j]:
                encrypted_message = encrypted_message + map_encrypted[j]
    return encrypted_message


print(cipher(alphabet))
print(encrypt("supercalifragilistichespiralidoso", alphabet))
