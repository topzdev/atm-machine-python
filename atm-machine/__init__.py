from register import registerMenu
users = []



def main():
    print("Choose module to enter")
    print("[1] Register")
    print("[2] Atm Machine")
    print("[3] Exit")

    choosen = input("Choose: ")

    if choosen == "1":
        registerMenu()

    elif choosen == "2":
        pass

    elif choosen == "3":
        exit(0)

    else: main()




main()