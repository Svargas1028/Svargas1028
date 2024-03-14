# VargasSandra
# February 27, 2024
# Simple Statistics Calculator
# This Python program calculates the sum, average, product, and largest value of four numbers provided by the user.

# Introduction
print("This program calculates simple statistics.")

# Instructions
print("Please enter four numbers to calculate their sum, average, product, and largest value.")

# Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Calculate sum, average, product, and largest value
total = num1 + num2 + num3 + num4
average = total / 4
product = num1 * num2 * num3 * num4
largest = max(num1, num2, num3, num4)

# Output results
print(f"{product:.0f} {average:.0f}")
print(f"{product:.3f} {average:.3f}")
