import random
import crud

def genPin():
    pin = ""
    for i in range(6):
        pin += str(random.randint(0,9))

    return pin

def location(acc_no):

    for user in crud.accounts:
        if user.accno == acc_no:
            return user

    return -1




