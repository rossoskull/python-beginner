a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

if a < b:
    c = a
    a = b
    b = c
gcd = 0
x = b
while x >= 1:
    if a % x == 0 and b % x == 0:
        gcd = x
        break
    x -= 1

print("The G.C.D of %d and %d is %d" % (a, b, gcd))

