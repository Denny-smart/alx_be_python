# daily_reminder

while True:
    # Prompt user for task details
    task = input("Enter your task (or 'q' to quit): ")
    if task.lower() == 'q':
        print("Goodbye!")
        break

    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Generate base message using match-case for priority
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level. Please enter high, medium, or low.\n")
            continue  # Restart loop if priority input is invalid

    # Add time sensitivity note
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    elif time_bound == "no":
        message += ". Consider completing it when you have free time."
    else:
        print("Invalid input for time sensitivity. Please enter yes or no.\n")
        continue  # Restart loop if time_bound input is invalid

    # Print the final customized reminder
    print("\nReminder:", message, "\n")
