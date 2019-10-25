import utils
from User import User
import config
import crud
active = User("","","","","","",0,"")

def login():
    global active
    crud.retrieve()
    print("Login")
    print("===========================================")
    acc_no = input("Enter your acconut number: ")
    pin = input("Enter your pin: ")

    user = utils.location(acc_no)
    user = crud.accounts[user]
    print(user)
    if user != -1:
        print(user.pin)
        if str(user.pin) == str(pin):
            active = user
            registerMenu()
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
        view_balance()
    elif choosen == "2":
        deposit()
    elif choosen == "3":
        widthdraw()
    elif choosen == "4":
        fund_transfer()
    elif choosen == "5":
        setting
    elif choosen == "6":
        login()


def view_balance():
    print("CURRENT BALANCE")
    print("===========================================================================================")
    print("Your Current Balance: Php", active.balance)
    utils.set_message("", registerMenu())


def deposit():
    print("DEPOSIT")
    print("===========================================================================================")
    print("Your Current Balance: Php", active.balance)
    deposit = float(input("Enter amount to deposit: Php "))

    utils.ask_continue()
    if utils.is_minimum(deposit):
        utils.set_message("The minimum amount to deposit is 500", deposit())
    elif utils.is_maximum(deposit):
        utils.set_message("The maximum amount to deposit is 500", deposit())
    else:
        active.balance += deposit
    if crud.update_balance(active.accno, active.balance):
        utils.set_message("The amount successfully deposited to your account", registerMenu())



def widthdraw():
    print("WIDTHDRAW")
    print("===========================================================================================")
    print("Your Current Balance: Php", active.balance)
    widthdraw = float(input("Enter amount to widthdraw : Php "))

    utils.ask_continue()
    if utils.is_minimum(widthdraw):
        utils.set_message("The minimum amount to widthraw is 500", widthdraw())
    elif utils.is_maximum(widthdraw):
        utils.set_message("The maximum amount to widthraw is 500", widthdraw())
    else:
        active.balance -= widthdraw

    if crud.update_balance(active.accno, active.balance):
        utils.set_message("Amount successfully widthdraw", registerMenu())



def fund_transfer():
    print("WIDTHDRAW")
    print("===========================================================================================")
    print("Your Current Balance: Php", active.balance)
    res_acc = input("Enter the Account Number of the reciever of money transfer :")
    amount = float(input("Enter the amount to transfer: Php "))

    res = utils.location(res_acc)
    res = crud.accounts[res]
    utils.ask_continue()
    if res:
       if utils.is_minimum(widthdraw):
           utils.set_message("The minimum amount to transfer is Php " + str(config.MIN_TRANSACTION), fund_transfer())
       elif utils.is_maximum(widthdraw):
           utils.set_message("The maximum amount to transfer is Php "+ str(config.MAX_TRANSACTION), fund_transfer())
       else:
           res_amount = res.balance + amount
           act_amount = active.balance - amount

       if crud.update_balance(res_acc, res_amount) and crud.update_balance(active.accno, act_amount):
           utils.set_message("Amount successfully transfered to " + res.get_fullname() + " amount of Php ", fund_transfer())

    else:
        utils.set_message("The Account Number of the reciever not found, please try again..", fund_transfer())


def setting():
    print("Choose module to enter")
    print("[1] Change Password")
    print("[2] Back")
    choosen = input("Choice: ")

    if choosen == "1":
        change_pin()
    elif choosen == "2":
        registerMenu()


def change_pin():
    print("CHANGE PIN")
    print("===========================================================================================")
    cur_pin = input("Enter the current pin: ")

    utils.ask_continue()
    if cur_pin == active.pin:
        new_pin = input("Enter the new pin: ")
        re_pin = input("Enter the re-enter pin: ")

        if new_pin == re_pin and crud.update_pin(active.accno, new_pin):
            utils.set_message("Pin successfully changed", registerMenu())
        else:
            utils.set_message("Pin not match, please try again..", change_pin())
    else:
        utils.set_message("Your inputted pin not match with your current pin, please try again..", change_pin())






