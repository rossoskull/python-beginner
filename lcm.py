a = int(input("Enter a number : "))
b = int(input("Enter another number : "))

if a < b:
    c = a
    a = b
    b = c

lcm = a
cond = 1
while cond == 1:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1
print("The L.C.M of %d and %d is %d." % (a, b, lcm))

