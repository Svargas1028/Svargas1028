# Sandra Vargas
# March 20, 2024
# P3HW2 - Employee Salary Calculation

# Pseudocode:
# 1. Ask the user to enter the name of the employee.
# 2. Ask the user to enter the number of hours the employee worked this week.
# 3. Ask the user to enter the employee's pay rate.
# 4. Check if the employee has worked overtime (more than 40 hours).
# 5. If yes, calculate the amount owed to the employee for overtime hours.
# 6. Calculate the amount the employee should be paid for regular hours worked.
# 7. Display gross pay (total amount that should be paid to the employee).
# 8. Display employee name, pay rate, number of hours worked, overtime hours, overtime pay, pay for regular hours, and gross pay.

# Ask the user to enter the employee's name
employee_name = input("Enter the employee's name: ")

# Ask the user to enter the number of hours worked this week
hours_worked = float(input("Enter the number of hours worked this week: "))

# Ask the user to enter the employee's pay rate
pay_rate = float(input("Enter the employee's pay rate per hour: "))

# Evaluate if the employee has worked overtime (more than 40 hours)
if hours_worked > 40:
    # Calculate the overtime hours worked
    overtime_hours = hours_worked - 40
    # Calculate the overtime pay (1.5 times the pay rate per hour)
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    # Calculate the pay for regular hours (first 40 hours)
    regular_pay = 40 * pay_rate
    # Calculate the gross pay (total amount to be paid to the employee)
    gross_pay = regular_pay + overtime_pay
else:
    # If no overtime worked, calculate only the pay for regular hours
    regular_pay = hours_worked * pay_rate
    # No overtime, so gross pay is equal to pay for regular hours
    gross_pay = regular_pay
    # Set overtime hours and overtime pay to zero
    overtime_hours = 0
    overtime_pay = 0

# Display the employee's salary summary in columns
print(f"----------------------------------------------------")
print(f"Employee Name: {employee_name}")
print(f"Hours Worked  Pay Rate  Overtime Hours  Overtime Pay  Regular Pay  Gross Pay")
print(f"-----------------------------------------------------------------------------")
print(f"{hours_worked:<13.2f} ${pay_rate:<8.2f} {overtime_hours:<15.2f} ${overtime_pay:<12.2f} ${regular_pay:<11.2f} ${gross_pay:.2f}")
