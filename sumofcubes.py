def sumNCubes(n):
    return sum(i**3 for i in range(1,n+1))

def main():
    n = int(input())
    print("Sum of cubes:", sumNCubes(n))

