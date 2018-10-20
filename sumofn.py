def summation_by_formula(n):
    return (n * (n+1)) // 2


if __name__ == "__main__":
    num = int(input("Enter the number until which you want to find the sum : "))
    print("The sum of first %d numbers is %d." % (num, summation_by_formula(num)))
