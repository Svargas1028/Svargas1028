# Sandra Vargas
# 3/14/2024
# P3LAB_VargasSandra
# This program determines if a given year is a leap year.

# Prompt the user to enter the year
print("Please enter a year:")
year = int(input())

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # If the year is divisible by 4 and not divisible by 100, or divisible by 400, it's a leap year
    print(f"{year} - leap year")
else:
    # Otherwise, it's not a leap year
    print(f"{year} - not a leap year")
