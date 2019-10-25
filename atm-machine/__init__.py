from register import registerMenu
from atm import login
users = []



def main():
    # login()
    print("Choose module to enter")
    print("[1] Register")
    print("[2] Atm Machine")
    print("[3] Exit")

    choosen = input("Choose: ")

    if choosen == "1":
        registerMenu()

    elif choosen == "2":
        login()

    elif choosen == "3":
        exit(0)

    else: main()




main()