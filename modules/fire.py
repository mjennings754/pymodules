import os
def burn(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        pass