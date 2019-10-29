
from config import SEED

def encrypt(pin):
    i = 0
    while(i < len(pin) ):
        pin = change_char(pin, i, str(chr(ord(pin[i]) + SEED)))
        i += 1
    return str(pin)

def decrpyt(pin):
    i = 0
    while (i < len(pin)):
        pin = change_char(pin, i, str(chr(ord(pin[i]) - SEED)))
        i += 1
    return str(pin)

def change_char(s, p, r):
    return s[:p]+r+s[p+1:]



#
# pin = encrypt("123456")
# print(pin)
#
#
pin = decrpyt("xv{z{|")
print((pin))