task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"Reminder: '{task}' is a {priority} priority task"

    case "low":
        message = f"Note: '{task}' is a {priority} priority task."

    case "medium":
        message = f"Reminder: '{task}' is a {priority} priority task."

    case _:
        message = f"Reminder: '{task}' has an unknown priority."

if time_bound == "yes":
    message += " that requires immediate attention today!"
elif time_bound == "no":
    message += " Consider completing it when you have free time."


print(message)