import random
import crud
import config
from os import system
from atm import registerMenu

def genPin():
    pin = ""
    for i in range(6):
        pin += str(random.randint(0,9))

    return pin

def location(acc_no):
    i = 0
    for user in crud.accounts:
        if user.accno == acc_no:
            return i
        i += 1

    return -1

def get_user(acc_no):
    acc_no = location(acc_no)
    return crud.accounts[acc_no]

def is_minimum(amount):
    return 1 if amount < config.MIN_TRANSACTION else 0

def is_maximum(amount):
    return 1 if amount > config.MAX_TRANSACTION else 0

def ask_continue():
    print("Do you want to continue ?")
    print("[1] Continue")
    print("[2] Discard")
    choice = input("Enter your choice : ")

    if choice == "1":
        pass
    elif choice == "2":
        registerMenu()
        return
    else:
        ask_continue()

def set_message(msg ,func):
    if msg != "": print(msg)
    input("Press any key to continue...")
    system("cls")
    func()
