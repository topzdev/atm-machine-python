import utils
from User import User
import config
import crud
import view
import card_detect
from Bycrypt import decrpyt
from os import system
active = User("","","","","",0,"","")


def card_verify():
    crud.retrieve()
    drive = card_detect.check_removable("1")
    acc_no = crud.get_card_number(drive)
    print(drive, acc_no, utils.location(acc_no))
    if utils.location(acc_no) != -1:
        login(acc_no)
    else:
        utils.set_message("Card has not been registered, Please register first the card...", card_verify)


def ask_remove_card():
    system("cls")
    print("Please remove your card")
    if card_detect.check_removable("2") != 0:
        card_verify()



def login(acc_no):
    global active
    view.logo()
    pin = input("Enter your pin: ")
    user = utils.location(acc_no)
    if user != -1:
        user = crud.accounts[user]
        if decrpyt(user.pin) == str(pin):
            active = user
            registerMenu()
        else:
            print("Wrong Pin!")

    else:
        print("Account number not exist!")



def registerMenu():
    view.header("MAIN MENU", active.get_fullname())
    print("[1] Balance Inquiry")
    print("[2] Deposit")
    print("[3] Quick Cash")
    print("[4] Widthdraw")
    print("[5] Fund Transfer")
    print("[6] Setting")
    print("[7] End of Transaction")
    choosen = input("Choice>>> ")

    if choosen == "1":
        view_balance()
    elif choosen == "2":
        deposit()
    elif choosen == "3":
        quick_cash()
    elif choosen == "4":
        widthdraw()
    elif choosen == "5":
        fund_transfer()
    elif choosen == "6":
        setting()
    elif choosen == "7":
        login()
    else:
        utils.set_message("Invalid input please try again...", registerMenu)


def view_balance():
    view.header("BALANCE INQUIRY",active.get_fullname())
    print("Your Current Balance: Php", active.balance)
    utils.ask_continue()
    ask_remove_card()


def deposit():
    view.header("DEPOSIT", active.get_fullname())
    print("Your Current Balance: Php", active.balance)
    deposit_amt = float(input("Enter amount to deposit: Php "))

    utils.ask_continue()
    if utils.is_minimum(deposit_amt):
        utils.set_message("The minimum amount to deposit is {}, Please try again".format(config.MIN_TRANSACTION), deposit)
    elif utils.is_maximum(deposit_amt):
        utils.set_message("The maximum amount to deposit is {}, Please try again".format(config.MAX_TRANSACTION), deposit)
    else:
        active.balance += deposit_amt
        if crud.update_balance(active.accno, active.balance):
            view.receipt(active,"1","",deposit_amt)
            ask_remove_card()



def widthdraw():
    view.header("WIDTHDRAW", active.get_fullname())
    print("Your Current Balance: Php", active.balance)
    widthdraw_amt = float(input("Enter amount to widthdraw : Php "))

    utils.ask_continue()
    if utils.is_sufficient(active.balance, widthdraw_amt):
        if utils.is_minimum(widthdraw_amt):
            utils.set_message("The minimum amount to widthraw is {}, Please try again".format(config.MIN_TRANSACTION), widthdraw)
        elif utils.is_maximum(widthdraw_amt):
            utils.set_message("The maximum amount to widthraw is {}, Please try again".format(config.MAX_TRANSACTION), widthdraw)
        else:
            active.balance -= widthdraw_amt
            if crud.update_balance(active.accno, active.balance):
                view.receipt(active, "2", "", widthdraw_amt)
                ask_remove_card()
    else:
        utils.set_message("Insufficient balance, Please try again", widthdraw)


def quick_cash():
    view.header("QUICK CASH", active.get_fullname())
    print("[1] 500  [2] 1000    [3] 2000    [4] 3000    [4] 10,000")
    chosen = input("Enter chosen number >>>")
    cash = 0
    if chosen == "1":
        cash = 500
    elif chosen == "2":
        cash = 1000
    elif chosen == "3":
        cash = 2000
    elif chosen == "4":
        cash = 3000
    elif chosen == "5":
        cash = 10000
    else:
        utils.set_message("Invalid chosen input, please try again...", quick_cash)

    print("The amount you want to widthraw is {}".format(cash))
    utils.ask_continue()
    if utils.is_sufficient(active.balance, cash):
        active.balance -= cash
        if crud.update_balance(active.accno, active.balance):
            view.receipt(active, "2","",cash)
            ask_remove_card()
    else:
        utils.set_message("Insufficient balance, Please try again", quick_cash)

def fund_transfer():
    view.header("FUND TRANSFER", active.get_fullname())
    print("Your Current Balance: Php", active.balance)
    res_acc = input("Enter the Account Number of the reciever of money transfer :")
    res = utils.location(res_acc)
    if res != -1:
        amount = float(input("Enter the amount to transfer: Php "))
        res = crud.accounts[res]
        utils.ask_continue()
        if utils.is_sufficient(active.balance, amount):
            if utils.is_minimum(amount):
                utils.set_message(
                    "The minimum amount to transfer is Php {}, Please try again".format(config.MIN_TRANSACTION),
                    fund_transfer)
            elif utils.is_maximum(amount):
                utils.set_message(
                    "The maximum amount to transfer is Php {}, Please try again".format(config.MAX_TRANSACTION),
                    fund_transfer)
            else:
                res_amount = res.balance + amount
                act_amount = active.balance - amount

                if crud.update_balance(res_acc, res_amount) and crud.update_balance(active.accno, act_amount):
                    view.receipt(active, "3", res_acc, amount)
                    ask_remove_card()
        else:
            utils.set_message("Insufficient balance, Please try again", fund_transfer)
    else:
        utils.set_message("The Account Number of the receiver not found, please try again..", fund_transfer)


def setting():
    view.header("SETTING", active.get_fullname())
    print("Choose module to enter")
    print("[1] Change Password")
    print("[2] Back")
    choosen = input("Choice: ")

    if choosen == "1":
        change_pin()
    elif choosen == "2":
        registerMenu()


def change_pin():
    view.header("CHANGE PIN", active.get_fullname())
    cur_pin = input("Enter the current pin: ")

    utils.ask_continue()
    if cur_pin == decrpyt(active.pin):
        new_pin = input("Enter the new pin: ")
        re_pin = input("Enter the re-enter pin: ")

        if new_pin == re_pin and crud.update_pin(active.accno, new_pin):
            utils.set_message("Pin successfully changed", ask_remove_card)
        else:
            utils.set_message("Pin not match, please try again..", change_pin)
    else:
        utils.set_message("Your inputted pin not match with your current pin, please try again..", change_pin)






