# python weekday.py
# It is the weekend, yay!

import datetime

def is_weekday():
    # Get the current day of the week 
    current_day = datetime.datetime.today().weekday()

    # Find out is the current day a weekday
    return current_day < 5

def answer():
    if is_weekday():
        print("Yes, unfortunately today is a weekday.")
    else:
        print("It is the weekend, yay!")
        
if __name__ == "__main__":
    answer()
    