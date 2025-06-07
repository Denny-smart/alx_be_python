# Multiplication table using a nested loop with repeated flow

while True:
    # Ask the user for a number or to quit
    user_input = input("Enter a number to see its multiplication table (or 'q' to quit): ")

    if user_input.lower() == 'q':
        print("Goodbye!")
        break

    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
        continue

    # Outer message
    print(f"\nMultiplication table for {number}:\n")

    # Nested loop to print the table
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

    print()  # Blank line for better spacing
