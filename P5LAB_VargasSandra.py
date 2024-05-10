# Sandra Vargas
# May 5, 2024
# Assignment: Leap Year Checker
# This program checks if a given year is a leap year or not.


def days_in_feb(user_year):
    if (user_year % 4 == 0 and user_year % 100 != 0) or (user_year % 400 == 0):
        return f"{user_year} has 29 days in February."
    else:
        return f"{user_year} has 28 days in February."

while True:
    input_year = input("Enter a year (or press Enter to exit): ")
    if not input_year.isdigit():
        break
    input_year = int(input_year)
    print(days_in_feb(input_year))
