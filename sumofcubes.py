def sum_of_cubes(n):
    # sum(i**3 for i in range(1, n+1))   # it was basic iterative approach try for mathematical approach!!
    return ((n * (n+1)) // 2) ** 2


if __name__ == "__main__":
    print("Sum of cubes:", sum_of_cubes(int(input("Enter Number: "))))
