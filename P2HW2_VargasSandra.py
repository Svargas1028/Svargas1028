# Sandra Vargas
# Date: 5 de marzo de 2024
# Assignment Name: Module Grades Calculator
# Brief description of program: This program calculates and displays the lowest grade, highest grade, sum of grades, and average grade based on user input for grades in six modules.

# Pseudocode:

# 1. Create an empty list to store grades.
# 2. Ask the user to enter grades for Module 1 to Module 6 one by one.
# 3. Add each entered grade to the list.
# 4. Calculate the lowest grade using the min() function on the list.
# 5. Calculate the highest grade using the max() function on the list.
# 6. Calculate the sum of all grades using the sum() function on the list.
# 7. Calculate the average grade by dividing the sum by the total number of grades.
# 8. Display the lowest grade, highest grade, sum of grades, and average grade.
# 9. Format the average grade to display only two decimal positions.


grades = []

grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print("------------Results-------------")
print("Lowest Grade:", lowest_grade)
print("Highest Grade:", highest_grade)
print("Sum of Grades:", sum_of_grades)
print("Average Grade: {:.2f}".format(average_grade))
print("--------------------------------")
