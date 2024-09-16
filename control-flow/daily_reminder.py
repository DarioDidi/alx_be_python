task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

message = f"Reminder: '{task}' is a"
#message = f"Reminder: '{task}' is a {priority} priority task"

match priority:
    case "high":
        message = f"{message} high priority task"
    case "medium":
        message = f"{message} medium priority task"
    case "low":
        message = f"{message} low priority task"
    case _:
        print("unknow priority")
        exit()
if time_bound == "yes":
    message = f"{message} that requires immediate attention today!"
else:
    message = f"{message }. Consider completing it when you have free time."

print(message)