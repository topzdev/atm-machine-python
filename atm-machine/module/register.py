from User import User
from _ccgen import completed_number
from utils import genPin
import crud

def registerMenu():

    crud.retrieve()
    print("Choose module to enter")
    print("[1] Register User")
    print("[2] Show Users")
    print("[3] Exit")

    choosen = input("Choose: ")

    if choosen == "1":
        registerInput()

    elif choosen == "2":
        showUsers()
    elif choosen == "3":
        exit(0)



def registerInput():

    user = User
    print("Register Account")
    print( "Personal Information")
    print( "=======================================================")
    fname = input("Enter your First Name: ")
    mname = input("Enter your Middle Name: ")
    lname = input("Enter your Last Name: ")
    email = input("Enter your Email Address: ")
    contact = input("Enter your Contact Number: ")
    balance = float(choosePlan())
    acc_no = completed_number(['6','4','2','9'], 16)
    pin = genPin()

    print("Your Initial balance: ", balance)
    print("Account number: ", acc_no)
    print("Account Pin number: ", pin)

    if crud.insert(user(fname, mname, lname, email, contact, balance, acc_no, pin)):
        crud.save()
        print("User successfully saved")




def choosePlan():
    balance = 0.0
    print("Choose Plan")
    print("======================================================")
    print("[1] STUDENT PLAN - Recommend for the student only need to present valid")
    print("    and the initial deposit is only 100.00 pesos" )
    print("[2] WORKER PLAN - Recommend for the workers who earn 10,000 to 100,000")
    print( "   only need to present valid and the initial deposit is only 3,000 pesos")
    print("[3] BUSSINESS PLAN - Recommend for the bussiness owner that want savings account")
    print("    and insurance at the sametime and who earn about 50,000 to 1,000,000 only" )
    print("    need to present bussiness certificate and BIR Record the initial deposit is")
    print("    only 100,000 pesos.")
    choice = input("Enter your choice: ")

    if choice == "1":
        balance = 100

    if choice == "2":
        balance = 3000

    if choice == "3":
        balance = 100000

    return balance


def showUsers():
    crud.display()
    print("End of line")
    input('Press any key...')
    registerMenu()