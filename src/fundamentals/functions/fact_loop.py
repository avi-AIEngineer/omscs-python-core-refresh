def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("Factorial of 5 is:", factorial(5))
    n = int(input("Enter a number to compute its factorial: "))
    print(f"Factorial of {n} is:", factorial(n))