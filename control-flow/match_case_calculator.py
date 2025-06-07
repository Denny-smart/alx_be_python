# Simple calculator with repeated flow

while True:
    # Get first number
    while True:
        num1_input = input("Enter the first number (or 'q' to quit): ")
        if num1_input.lower() == 'q':
            print("Goodbye!")
            exit()
        try:
            num1 = int(num1_input)
            break  # valid input, break inner loop
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get second number
    while True:
        num2_input = input("Enter the second number (or 'q' to quit): ")
        if num2_input.lower() == 'q':
            print("Goodbye!")
            exit()
        try:
            num2 = int(num2_input)
            break  # valid input, break inner loop
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get operation
    operation = input("Choose the operation (+, -, *, /): ")

    match operation:
        case "+":
            print(f"The result is: {num1 + num2}\n")
        case "-":
            print(f"The result is: {num1 - num2}\n")
        case "*":
            print(f"The result is: {num1 * num2}\n")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.\n")
            else:
                print(f"The result is: {num1 / num2}\n")
        case _:
            print("Invalid operation.\n")
