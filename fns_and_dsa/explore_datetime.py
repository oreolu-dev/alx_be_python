import datetime


def display_current_datetime():
    current_datetime = datetime.datetime.now()

    # Formating as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Printing the formatted date and time
    print(f"Current date and time: {formatted_datetime}")



def calculate_future_date(number_of_days):
    # Get the current date
    current_date = datetime.date.today()

    # Calculate the future date by adding the number of days
    future_date = current_date + datetime.timedelta(days=number_of_days)

    # Print the future date in "YYYY-MM-DD" format
    print(f"Future date: {future_date}")



def main():
    display_current_datetime()

    number_of_days = int(input("Enter the number of days to add to the current date: "))

    calculate_future_date(number_of_days)


if __name__ == "__main__":
    main()
