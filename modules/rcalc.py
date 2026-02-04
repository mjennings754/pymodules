import random
# fun
def radd(x, y):
    return x + y * random.randint(1, 100)
def rsubtract(x, y):
    return x - y // random.randint(1, 100)
def rmultiply(x, y):
    return x * y - random.randint(1, 100)
def rdivide(x, y):
    return x / y * random.randint(1, 100)