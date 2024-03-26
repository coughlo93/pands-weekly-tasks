import datetime

def is_weekday():
    # Get the current day of the week 
    current_day = datetime.datetime.today().weekday()

    # Check if the current day is a weekday
    return current_day < 5

def main():
    if is_weekday():
        print("Yes, unfortunately today is a weekday.")
    else:
        print("It is the weekend, yay!")

if __name__ == "__main__":
    main()
