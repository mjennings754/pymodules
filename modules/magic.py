import random
def disappear(s):
    return "".join(
        char if random.random() > 0.3 else " "
        for char in s
    )

def magic_add(s):
    return "".join(
        char if random.random() > 0.5 else f"{random.randint(1, 100)}"
        for char in s
    )