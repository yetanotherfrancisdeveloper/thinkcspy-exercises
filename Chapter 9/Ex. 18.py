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
