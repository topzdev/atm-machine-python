import utils
from User import User
import crud
active = User("","","","","","","","")

def login():
    global active
    crud.retrieve()
    print("Login")
    print("===========================================")
    acc_no = input("Enter your acconut number: ")
    pin = input("Enter your pin: ")

    user = utils.location(acc_no)

    if user != -1:
        print(user.pin)
        if str(user.pin) == str(pin):
            active = user
            print(active.pin)
        else:
            print("Wrong Pin!")

    else:
        print("Account number not exist!")



def registerMenu():

    print("Choose module to enter")
    print("[1] View Balance")
    print("[2] Deposit")
    print("[3] Widthraw")
    print("[4] Fund Transfer")
    print("[5] Setting")
    print("[6] End of Transaction")
    choosen = input("Choice: ")

    if choosen == "1":
        pass
    elif choosen == "2":
        pass
    elif choosen == "3":
        pass
    elif choosen == "4":
        pass
    elif choosen == "5":
        pass
    elif choosen == "6":
        pass





