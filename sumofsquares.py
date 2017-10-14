n = int(input("Enter the number till which you want the sum of squares : "))
sumS=0
for x in range(1,n+1):
    sumS += x**2

print("The sum of squares till first %d numbers is %d." % (n, sumS))
