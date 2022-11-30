
inputarray = []
idarru = []
idarrl = []
unlocked = False
code = False

while 1:
    while code == False:
        print("please enter the last 5 digits of student id")
        id = input()
        if len(id) == 5 and id.isnumeric() == True:
            for x in id:
                idarru.append(int(x))
                idarrl.append(int(x))
            idarru.append(1)
            idarrl.append(4)
            print("valid id entered")
            print("Use the code to lock or unlock the machine, Enter code 1 digit at a time")
            print("Press E (uppercase) to exit")
            code = True
        else:
            print("invalid id")

    print("enter a digit")
    dig = input()

    if dig == "E":
        break

    if dig.isdigit() == True and len(dig) == 1:
        inputarray.append(int(dig))

    if len(inputarray) > 6:
        inputarray.pop(0)

    if inputarray == idarru and unlocked == False:
        print("UNLOCKED")
        unlocked = True
    elif inputarray == idarru and unlocked == True:
        print("lock already unlocked, use locking code to lock")
    elif inputarray == idarrl and unlocked==False:
        print("Lock is locked, use unlocking code to unlock")
    elif inputarray == idarrl and unlocked == True:
        print("LOCKCED")
        unlocked = False

    
    





    
