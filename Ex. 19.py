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
                    encrypted_message = encrypted_message + mapping[0]
                elif i == " ":
                    encrypted_message = encrypted_message + " "
                else:
                    encrypted_message = encrypted_message + mapping[j + 1]
    return encrypted_message


def decrypter(encrypted_message, coder):
    """Deciphers the given encrypted message with the code used above to encrypt it."""
    decrypted_message = ""
    coder_len = len(coder)
    for i in encrypted_message:
        for j in range(coder_len):
            if i == coder[j]:
                if j == coder[0]:
                    decrypted_message = decrypted_message + coder[coder_len - 1]
                else:
                    decrypted_message = decrypted_message + coder[j - 1]
    return decrypted_message.capitalize()


code = encrypt(alphabet, alphabet)
encrypted = encrypt("Samantha", alphabet)
decrypted = decrypter(encrypted, code)
print(code)
print(encrypted)
print(decrypted)
