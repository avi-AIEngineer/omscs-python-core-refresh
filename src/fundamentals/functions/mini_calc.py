def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def advanced_calculator():
    """Advanced calculator with multiple numbers"""
    print("=== Advanced Calculator ===")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                numbers = input("Enter numbers separated by spaces: ").split()
                numbers = [float(num) for num in numbers]
                
                if choice == '1':
                    result = numbers[0]
                    for num in numbers[1:]:
                        result = add(result, num)
                    print(f"Result: {result}")
                elif choice == '2':
                    result = numbers[0]
                    for num in numbers[1:]:
                        result = subtract(result, num)
                    print(f"Result: {result}")
                elif choice == '3':
                    result = numbers[0]
                    for num in numbers[1:]:
                        result = multiply(result, num)
                    print(f"Result: {result}")
                elif choice == '4':
                    result = numbers[0]
                    for num in numbers[1:]:
                        result = divide(result, num)
                    print(f"Result: {result}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")

def calculator():
    """Mini calculator with user interaction"""
    print("=== Mini Calculator ===")
    print("Select operation:")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"Result: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter valid numbers.")
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    print("Do you want to use basic mode (2 numbers) or advanced mode (multiple numbers)?")
    mode = input("Enter 'basic' or 'advanced': ").lower()
    
    if mode == 'advanced':
        advanced_calculator()
    else:
        calculator()