
#SIMPLE BANK PROGRAM WHERE USERS CAN CREATE ACCOUNTS AND CARRY OUT TRANSACTIONS
#BY JAY MISTRY

#OBJECT DECLARATION:
class Account():
    def __init__(self, name, id, pin, bal):
        self.name = name
        self.id = id
        self.pin = pin
        self.bal = float(bal)

    def getName(self):
        print("Name of Account Holder : "+self.name)

    def getId(self):
        print("ID of Account Holder : " + self.id)

    def getPass(self):
        print("PIN of Account Holder : ")

    def getBal(self):
        print("Current Balance of Account Holder : " + self.bal)

    def changeBal(self, x):
        self.bal = self.bal + x


#DEFINE FUNCTIONS: --------------------------------------------
def printMenu():
    print("Select one of the options below: \n1) New Account\n2) Display Account\n3) Transactions\n4) Exit")
    while True:
        try:
            x = int(input(r"Enter your choice here (1\2\3\4): "))
            if x > 4 or x < 1:
                raise ValueError
            break
        except:
            print("Please enter either 1, 2, 3, or 4 and press enter")
    return x



def waitUser():
    input("Press Enter To Continue...\n\n\n\n\n")



def getUAndCheck(List):
    id = str(input("Enter your ID : "))
    pin = str(input("Enter your PIN : "))

    x = getIndex(List,id, pin)

    return x



def getIndex(List, id, pin):
    n=0
    case = 1

    for x in List:
        if (id == x.id) and (pin == x.pin):

            return n
            case = 0

        n = n+1
    if case is 1:
        return -1



# -------------------------------------------------------


#MAIN CODE:
print(("Welcome to JM Bank ( Python Division ) !"))
state = 0
temp = Account("a", "a", "a", 0)
objList = [temp]
while True:
    x = printMenu()

    if x is 1:
        name = str(input("Enter Your Name : "))
        while True:
            id = str(input("Enter ID Of Your Choice : "))
            idpresent = 0
            if state is not 0 :
                for x in objList:
                    if x.id == id:
                        idpresent = 1

            if idpresent is 1:
                print("ID Already Occupied! Please Try Again.")
                continue
            else:
                break


        pin = str(input("Enter PIN Of Your Choice : "))
        c = str(input("Would You Like To Initiate Your Account With An Initial Balance? (y/n) : "))
        if (c is 'y') or (c is 'Y'):
            while True:
                try:
                    bal = float(input("Enter Your Amount : "))
                    break
                except ValueError:
                    print("Please Enter An Amount In Numbers! ")

        else:
            bal = 0


        temp = Account(name, id, pin, bal)

        if state is 0:
            objList = [temp]
            state = 1
        else:
            objList.append(temp)
        waitUser()

    elif x is 2:
        if (len(objList) is 1) and (state is 0):
            print("No Accounts To Display!")
            waitUser()
            continue

        v = getUAndCheck(objList)

        if v is -1:
            print("No Such Account Exists! ")
        else:
            print("Name of the Account Holder : " + objList[v].name)
            print("Available Balance : " + str(objList[v].bal))

        waitUser()

    elif x is 3:
        if (len(objList) is 1) and (state is 0):
            print("No Accounts To Display!")
            waitUser()
            continue

        v = getUAndCheck(objList)

        if v is -1:
            print("No Such Account Exists! ")
        else:
            print("Name of the Account Holder : " + objList[v].name)
            print("Available Balance : " + str(objList[v].bal))
            print("What Would You Like To Do? Credit Or Debit ( c/d )")
            while True:
                x = str(input("Enter your Choice : "))
                if (x is 'c') or (x is 'C'):
                    am = float(input("Enter the amount : "))
                    break

                elif (x is 'd') or (x is 'D'):
                    am = float(input("Enter the amount : "))
                    break

                else:
                    print("Enter Correct Value!")
                    continue

            if ( (objList[v].bal-am)<0 ):
                print("You Do Not Have Enough Balance!")

            else:
                print("Previous Balance : " + str(objList[v].bal))
                if (x is 'c') or (x is 'C'):
                    am = am*(-1)
                objList[v].bal = objList[v].bal + am
                print("New Balance : " + str(objList[v].bal))
            waitUser()
    elif x is 4:
        print("Thank You For Using JM Bank ( Python Division ).")
        waitUser()
        break
