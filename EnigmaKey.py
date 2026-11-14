from datetime import datetime as dt
import random

def EKey():
    t = dt.now()

    TheKey = ((
        t.year +
        t.month   +
        t.day  +
        t.hour  +
        t.minute  +
        t.second)  + (t.microsecond*10000)) // 10000

    rng = random.Random(TheKey)

    rotors = rng.sample([1, 2, 3, 4, 5], 3)

    positions = [
        rng.randint(0, 25),
        rng.randint(0, 25),
        rng.randint(0, 25)
    ]

    reflector = rng.choice(["A", "B", "C"])

    return {
        "key": TheKey,
        "rotors": rotors,
        "positions": positions,
        "reflector": reflector
    }

print(EKey())
