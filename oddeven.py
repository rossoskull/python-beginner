import sys

def checkOE(a):
    if(a%2==0):
        return "The number is even"
    elif a==1:
        return "The number is neither odd nor even"
    else :
        return "The number is odd"

print("Enter a number : ")
x = int(sys.stdin.readline())
print(checkOE(x))
