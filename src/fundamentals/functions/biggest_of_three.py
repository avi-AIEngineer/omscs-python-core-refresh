from time import sleep


def biggest_of_three(a, b, c):
    return max(a, b, c)

if __name__ == "__main__":
    sample = (5, 10, 3)
    print("Output:", biggest_of_three(*sample))
    sleep(5)    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    print("Biggest is:", biggest_of_three(a, b, c))