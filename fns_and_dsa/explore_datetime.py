from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    num_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=num_days)
    future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {future_date}")
    
# if __name__ == "__main__":
#     display_current_datetime()
#     calculate_future_date()