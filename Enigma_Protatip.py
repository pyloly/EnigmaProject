import random
import string
import EnigmaKey


def generate_cipher():
    key = EnigmaKey.TheKey
    alphabet = list(string.ascii_uppercase + "!@#$%^&*+-/? ")
    rng = random.Random(key)
    shuffled = alphabet.copy()
    rng.shuffle(shuffled)
    cipher = dict(zip(alphabet, shuffled))

    return cipher, key


def encrypt(text, cipher):
    result = ""
    for char in text.upper():
        if char in cipher:
            result += cipher[char]
        else:
            result += char
    return result


def decrypt(text, cipher):
    reverse_cipher = {value: key for key, value in cipher.items()}
    result = ""
    for char in text:
        if char in reverse_cipher:
            result += reverse_cipher[char]
        else:
            result += char
    return result


# cipher, key = generate_cipher()

# print("=== ENIGMA PYTHON ===")
# print("Ключ:", key)
#
# text = input("Введите текст: ")
#
# encrypted = encrypt(text, cipher)
# print("Зашифровано:", encrypted)
#
# decrypted = decrypt(encrypted, cipher)
# print("Расшифровано:", decrypted)
#
# cipher, key = generate_cipher()
# print("=== ENIGMA PYTHON ===")
# print("Ключ:", key)
# text = input("Введите текст: ")
# encrypted = encrypt(text, cipher)
# print(encrypted)