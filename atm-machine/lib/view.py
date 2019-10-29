import config
import utils
from datetime import datetime
from os import system
# from atm import active
now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")



def receipt(active, mode, trans_acc, amount):
    # print('\n'*5)
    system("cls")
    balance = float(active.balance)
    print("===================================================")
    print("  ████████╗    ██████╗     ██████╗ ")
    print("  ╚══██╔══╝    ██╔══██╗    ██╔══██╗")
    print("     ██║       ██████╔╝    ██████╔╝")
    print("     ██║       ██╔══██╗    ██╔═══╝ ")
    print("     ██║       ██████╔╝    ██║     ")
    print("     ╚═╝       ╚═════╝     ╚═╝   ")
    print("===================================================")
    print("{} ({})".format(config.CMPY_NAME, config.CMPY_SHORT))
    print("===================================================")
    print("TRANSACTION TIME: {}".format(current_time))
    print("CUSTOMER NAME: {}".format(active.get_fullname().upper()))
    print("===================================================")
    print("ACCNT NUM: {}".format(active.accno))

    if mode == "1":
        print("AMT DEPOSIT: PHP {}".format(amount))
    elif mode == "2":
        print("AMT WIDTHRAW: PHP {}".format(amount))
    else:
        print("AMT TRANSFERED: PHP {}".format(amount))
        print("RECEIVER ACCT NO: {}".format(trans_acc))
        print("AMT TRANSFERED TO: {}".format(utils.get_user(trans_acc).get_fullname().upper()))

    print("AVAIL BALANCE : PHP {}".format(balance))
    print("Thanks for trusting us, Have good day!")
    print("Please keep the receipt for more info.." )
    print("===========================================")
    input("Press any key to continue...")


def logo():
    # print('\n' * 30)
    system("cls")
    print("=======================================")
    print("  ████████╗    ██████╗     ██████╗ ")
    print("  ╚══██╔══╝    ██╔══██╗    ██╔══██╗")
    print("     ██║       ██████╔╝    ██████╔╝")
    print("     ██║       ██╔══██╗    ██╔═══╝ ")
    print("     ██║       ██████╔╝    ██║     ")
    print("     ╚═╝       ╚═════╝     ╚═╝   ")
    print("=======================================")
    print(" TECHNOLOGICAL BANK OF THE PHILIPPINES ")
    print("=======================================")


def header(title,fullname):
    # print('\n' * 30)
    system("cls")
    print("\n=====================================================================")
    print(config.CMPY_NAME.upper())
    print("{} ======================================= {}".format(title,current_time))
    print("Hi!,{}".format(fullname))
    print("=====================================================================")
