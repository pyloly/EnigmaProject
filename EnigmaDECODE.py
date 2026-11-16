import random

def generate_settings(key):
    rng = random.Random(key)
    rotors = rng.sample([1, 2, 3, 4, 5], 3)
    positions = [ rng.randint(0, 25), rng.randint(0, 25), rng.randint(0, 25)]
    reflector = rng.choice(["A", "B", "C"])
    return rotors, positions, reflector




def find_key(target_rotors, target_positions, target_reflector):
    matches = []
    for key in range(1000000):
        rotors, positions, reflector = generate_settings(key)
        if (rotors == target_rotors and
            positions == target_positions and
            reflector == target_reflector):
            matches.append(key)
    return matches[0]


# result = find_key(
#     [1, 5, 4],
#     [0, 7, 25],
#     "A"
# )
# # {'key': 600641, 'rotors': [1, 5, 4], 'positions': [0, 7, 25], 'reflector': 'A'}
# print("ключ:", result)