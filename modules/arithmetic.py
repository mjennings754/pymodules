__all__ = ["add", "subtract", "multiply", "divide", "add_multiple"]

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add_multiple(*args):
    return sum(args)
