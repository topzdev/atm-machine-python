import utils,card_detect, config,crud, view, input as inp
from User import User
from Bycrypt import decrpyt
from os import system
from time import sleep
import getpass
active = User
attempts = 0

def card_verify():
    crud.retrieve()
    drive = card_detect.check_removable("1")
    acc_no = crud.get_card_number(drive)
    # print(drive, acc_no, utils.location(acc_no))
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
    # pin = getpass.getpass(prompt='Enter your pin: ')
    pin = inp.pin_getter()
    user = utils.location(acc_no)
    if user != -1:
        user = crud.accounts[user]
        if decrpyt(user.pin) == str(pin):
            active = user
            registerMenu()
        else:
            print("\n")
            attemps_count(acc_no)

    else:
        print("Account number not exist!")

def trans_verify(func_call):
    view.logo()
    pin = inp.pin_getter()
    global active
    if decrpyt(active.pin) == str(pin):
        func_call()
    else:
        utils.set_message("Wrong pin", registerMenu)



def attemps_count(acc_no):
    global attempts
    attempts += 1
    timer = 0
    message = ""
    if(attempts >=2 and attempts <=4):
        message = "Wrong pin, {} attemps you made, wait till ".format(attempts)
        # print("{} attemps you made, wait till ".format(attempts))
        timer = 60
    elif(attempts >=5 and attempts <=6):
        message = "Warning more than 7 attemps will terminate your transaction, wait till "

        timer = 120
    elif(attempts >= 7):
        print("Program terminated")
        exit(0)
    else:
        login(acc_no)
        return

    while timer > 0:
        system("cls")
        view.logo()
        print(message)
        print("{} seconds".format(timer))
        sleep(1)
        timer-=1

    login(acc_no)



def registerMenu():
    view.header("MAIN MENU", active.get_fullname())
    print("[1] Balance Inquiry")
    print("[2] Deposit")
    print("[3] Quick Cash")
    print("[4] Withdraw")
    print("[5] Fund Transfer")
    print("[6] Setting")
    print("[7] End of Transaction")
    choosen = input("Choice>>> ")

    if choosen == "1":
        trans_verify(view_balance)
    elif choosen == "2":
        trans_verify(deposit)
    elif choosen == "3":
        trans_verify(quick_cash)
    elif choosen == "4":
        trans_verify(widthdraw)
    elif choosen == "5":
        trans_verify(fund_transfer)
    elif choosen == "6":
        trans_verify(setting)
    elif choosen == "7":
        ask_remove_card()
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
    print("[1] 500  [2] 1000    [3] 2000    [4] 3000    [5] 10,000")
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
        trans_verify(change_pin)
    elif choosen == "2":
        registerMenu()


def change_pin():
    view.header("CHANGE PIN", active.get_fullname())
    print("Enter your current pin to verify")
    cur_pin = inp.pin_getter()

    utils.ask_continue()
    if cur_pin == decrpyt(active.pin):
        print("\nEnter your new pin")
        new_pin = inp.pin_getter()
        print("\nRe-enter your pin")
        re_pin = inp.pin_getter()

        if new_pin == re_pin and crud.update_pin(active.accno, new_pin):
            utils.set_message("Pin successfully changed", ask_remove_card)
        else:
            utils.set_message("Pin not match, please try again..", change_pin)
    else:
        utils.set_message("Your inputted pin not match with your current pin, please try again..", change_pin)






