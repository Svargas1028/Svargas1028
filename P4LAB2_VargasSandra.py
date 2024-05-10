# Sandra Vargas
# March 26, 2024
# P4LAB2
# Output Range with Increment of 5
# A Python program that takes two integers as input and outputs the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer.

def display_increment(start, end):
    if end < start:
        return "Second integer can't be less than the first."
    
    result = ''
    current = start
    while current <= end:
        result += str(current)
        current += 5
        if current <= end:
            result += ' '

    return result

# Input the two integers
try:
    first_int = int(input("Enter the first integer: "))
    second_int = int(input("Enter the second integer: "))
    
    output = display_increment(first_int, second_int)
    print(output)
except ValueError:
    print("Error: Please enter valid integers.")
