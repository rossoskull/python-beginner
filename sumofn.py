n = int(input("Enter the number until which you want to find the sum : "))
sumS = 0
for x in range(1,n+1):
    sumS += x

print("The sum of first %d numbers is %d." % (n, sumS))
