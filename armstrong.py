a = int(input("Enter a number : "))
nOfDigits = len(str(a))
temp = a
x=0
arm=0
while x < nOfDigits:
    arm += int(temp%10)**(nOfDigits)
    temp= int(temp/10)
    x+=1
if arm == a:
    print("The number is an Armstrong number.")
else :
    print("The number is not an Armstrong number.")
