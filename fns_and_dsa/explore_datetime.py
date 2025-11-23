from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the output
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days_to_add):
    # Get today's date
    current_date = datetime.now()
    
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format future date
    formatted_future = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future}")


def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Ask user for number of days
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
