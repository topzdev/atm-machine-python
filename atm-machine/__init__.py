from register import registerMenu
from atm import card_verify, login
import view
users = []



def main():
    view.logo()
    print("Choose module to enter")
    print("[1] Register")
    print("[2] Atm Machine")
    print("[3] Exit")

    choosen = input("Choose>>> ")

    if choosen == "1":
        registerMenu()

    elif choosen == "2":
        card_verify()

    elif choosen == "3":
        exit(0)

    else: main()




main()