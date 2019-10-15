import random

def genPin():
    pin = ""
    for i in range(6):
        pin += str(random.randint(0,9))

    return pin