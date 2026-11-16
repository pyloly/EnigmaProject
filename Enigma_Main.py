
def encode(numbers):
    return "o".join(str(num).zfill(2) for num in numbers)


def decode(code):
    return [int(num) for num in code.split("o")]


# numbers = [22, 9, 25]
# encrypted = encode(numbers)
# decrypted = decode(encrypted)
# print(encrypted)
# print(decrypted)
