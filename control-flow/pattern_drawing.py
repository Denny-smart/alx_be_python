# pattern_drawing

while True:
    # Prompt the user for pattern size or to quit
    user_input = input("Enter the size of the pattern (or 'q' to quit): ")

    # Exit the loop if the user types 'q'
    if user_input.lower() == 'q':
        print("Goodbye!")
        break

    # Try converting input to an integer
    try:
        size = int(user_input)

        # Check if the number is positive
        if size <= 0:
            print("Please enter a positive number.\n")
            continue

        # Print square pattern using nested loops
        row = 0
        while row < size:
            for _ in range(size):
                print("*", end="")  # Print asterisk without newline
            print()  # Move to the next line after each row
            row += 1

        print()  # Add a blank line before next input

    except ValueError:
        print("Invalid input. Please enter a number.\n")
