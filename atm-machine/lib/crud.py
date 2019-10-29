from User import User
import utils
import config
import card_detect
import Bycrypt
import os
accounts = []

def insert(data):
    global accounts
    accounts.append(data)
    return 1

def update_balance(acc_no, amount):
    global accounts
    idx = utils.location(acc_no)
    accounts[idx].balance = amount
    save()
    return 1

def update_pin(acc_no, pin):
    global accounts
    idx = utils.location(acc_no)
    accounts[idx].pin = Bycrypt.encrypt(pin)
    save()
    return 1

def display():
    global  accounts
    for account in accounts:
        print("{} {} {} {} {} {} {} {}".format(account.fname, account.mname,account.lname,account.email,account.contact,account.balance,account.accno,""))
        # print(account.fname+' '+account.mname+' '+account.lname+' '+account.email+' '+account.contact+' '+account.balance+' '+account.accno+' '+account.pin)

def save():
    global accounts
    with open("database.txt", 'w') as file:
        for account in accounts:
            file.write("{} {} {} {} {} {} {} {}\n".format(account.fname, account.mname,account.lname,account.email,account.contact,account.balance,account.accno,account.pin))

def retrieve():
    global accounts
    accounts = []
    with open("database.txt",'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.split(' ')
            insert(User(line[0], line[1], line[2], line[3], line[4], float(line[5]), line[6], line[7].strip()))


def save_to_card(path, acc_no):
    with open("{}:\\{}".format(path, config.FILE_NAME),'w') as file:
        file.write(acc_no)

def get_card_number(path):
    print(card_detect.is_card_exist(path))
    if card_detect.is_card_exist(path):
        with open("{}:\\{}".format(path, config.FILE_NAME),'r') as file:
            return file.readline()