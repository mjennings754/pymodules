import random
def disappear(s):
    return "".join(
        char if random.random() > 0.3 else " "
        for char in s
    )