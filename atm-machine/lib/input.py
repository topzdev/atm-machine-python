import msvcrt
def pin_getter():
    print("-----------Enter your pin------------"),
    chars=[]
    i = 0
    while True:
        newChar=msvcrt.getch().decode('utf-8')
        if i >= 6 or newChar in '\r\n' :
            break
        elif newChar=='\b':
            if chars and i != 0:
                del chars[-1]
                msvcrt.putch('\b'.encode('utf-8'))
                msvcrt.putch(' '.encode('utf-8'))
                msvcrt.putch('\b'.encode('utf-8'))
                i -= 1;
        else:
            chars.append(newChar)
            msvcrt.putch('*'.encode('utf-8'))
            i +=1;
    return ''.join(chars)

# print(pin_getter())