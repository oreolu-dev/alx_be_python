from datetime import datetime, timedelta, date

def display_current_datetime():
    current_datetime = datetime.now()

    # Formatting as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date(number_of_days):
    current_date = date.today()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date}")

def main():
    display_current_datetime()

    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(number_of_days)

if __name__ == "__main__":
    main()
