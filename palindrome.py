import sys
x = int(input("Enter a number : "))
temp = x
cond = 1
palindrome = 0
while(cond==1):
    if ((len(str(int(temp))) >= 1) and (temp != 0)):
        palindrome = palindrome*10 + int(temp%10)
        temp = int(0.1*temp)

    else :
        cond = 0

print("The reverse is : %d" % (palindrome))
if palindrome == x:
    print("The number is a palindrome.")
else :
    print("The number is not a palindrome")
