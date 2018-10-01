def factorial(num):
    num = int(num)
    fac = 1
    while(num > 0):
        fac *= num
        num -= 1
    return fac

if __name__ == '__main__':
    num = input("Enter a number: ")
    print("fact({0}) = {1}".format(num, factorial(num)))