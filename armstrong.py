a = int(input("Enter a number : "))
number_of_digits = len(str(a))
temp = a
x, arm = 0, 0
while x < number_of_digits:
    arm += int(temp % 10) ** number_of_digits
    temp = int(temp / 10)
    x += 1
if arm == a:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
