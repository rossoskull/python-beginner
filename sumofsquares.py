def summation_by_formula(n):
    return (n * (n+1) * (2*n + 1)) // 6


if __name__ == "__main__":
    num = int(input("Enter the number till which you want the sum of squares : "))
    print("The sum of squares till first %d numbers is %d." % (num, summation_by_formula(num)))
