from User import User
accounts = []

def insert(data):
    global accounts
    accounts.append(data)
    save()
    print("User successfully saved")

def display():
    global  accounts

    for account in accounts:
        print(account.fname+' '+account.mname+' '+account.lname+' '+account.email+' '+account.contact+' '+account.balance+' '+account.accno+' '+account.pin+'\n')

def save():
    global accounts
    with open("database.txt", 'w') as file:
        for account in accounts:
            file.write(account.fname+' '+account.mname+' '+account.lname+' '+account.email+' '+account.contact+' '+str(account.balance)+' '+account.accno+' '+account.pin)
            file.write('\n')

def retrieve():
    global accounts
    with open("database.txt",'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.split(' '))
            line = line.split(' ')
            insert(User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7]))
            print(line[6])



