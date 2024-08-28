# Simple calculator program

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

print("Simple Calculator")
print("Available operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user input
operation = input("Enter operation (add/subtract/multiply/divide): ").strip().lower()

if operation in ['add', 'subtract', 'multiply', 'divide']:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == 'add':
            result = add(num1, num2)
        elif operation == 'subtract':
            result = subtract(num1, num2)
        elif operation == 'multiply':
            result = multiply(num1, num2)
        elif operation == 'divide':
            result = divide(num1, num2)
        
        print(f"The result is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
else:
    print("Invalid operation. Please choose from add, subtract, multiply, or divide.")
