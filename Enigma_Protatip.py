import random
import string
from datetime import datetime

def generate_cipher():
    t = datetime.now()
    key = (
        t.year + t.month * 13 + t.day * 17 +
        t.hour * 19 + t.minute * 23 +
        t.second * 29 + (t.microsecond // 1000) * 997
    ) % 1000000
    alphabet = list(string.ascii_uppercase + "!@#$%^&*+-/?")
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
    reverse_cipher = {v: k for k, v in cipher.items()}
    result = ""
    for char in text:
        if char in reverse_cipher:
            result += reverse_cipher[char]
        else:
            result += char
    return result


cipher, key = generate_cipher()
print("=== ENIGMA PYTHON ===")
print("Ключ:", key)
text = input("Введите текст: ")

encrypted = encrypt(text, cipher)


print(encrypted)

print("Расшифрованный текст:")
print(decrypt(encrypted, cipher))