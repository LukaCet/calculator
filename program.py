user_input = input("Enter an expression (e.g., num1 + num2): ")
parts = user_input.split()
if len(parts) != 3:
    print("Invalid input format. Please use 'num1 operator num2' format with spaces.")
else:
    num1 = int(parts[0])
    operator = parts[1]
    num2 = int(parts[2])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Division by zero is not allowed.")
            result = None
    else:
        print("Invalid operator. Please use +, -, *, or /.")

    if result is not None:
        print(f"Answer: {result}")
