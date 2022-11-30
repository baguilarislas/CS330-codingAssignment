
import time
import random
inputarray = []
digits = [1,2,3,4,5,6,7,8,9,0]
startTime = 0
c = 0
endTime = 0
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
            startTime = time.time()
            code = True
        else:
            print("invalid id")

    dig = random.choice(digits)
    inputarray.append(dig)

    print("attempt" + str(c))


    if len(inputarray) > 6:
        inputarray.pop(0)

    print(inputarray)

    if inputarray == idarru and unlocked == False:
        print("UNLOCKED")
        endTime = time.time() - startTime
        print("Time to unlock was:" + str(endTime))
        print("unlocked in " + str(c) + " attempts")
        unlocked = True
        break
    c += 1

    
    





    
