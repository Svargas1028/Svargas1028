# February 27, 2024
# P2HW1: Travel Budget Calculator (Updated)
# Calculates the remaining budget for a trip

# Get user input
budget = float(input("Enter your budget (in dollars): "))
destination = input("Enter your travel destination: ")
gasoline_cost = float(input("How much do you think you will spend on gas: "))
hotel_cost = float(input("Approximately, how much do you think you will spend on accommodation: "))
food_cost = float(input("How much do you think you will spend on food: "))

# Calculate total expenses and remaining budget
total_expenses = gasoline_cost + hotel_cost + food_cost 
remaining_budget = budget - total_expenses

# Print all expenses entered by the user
print("-" * 9 + " Travel Expenses " + "-" * 9)
print(f"Destination:       {destination}")
print(f"Initial budget:    ${budget:.2f}")
print(f"Gasoline cost:     ${gasoline_cost:.2f}")
print(f"Hotel cost:        ${hotel_cost:.2f}")
print(f"Food cost:         ${food_cost:.2f}")

# Print a dividing line
print("-" * 25)

print(f"Remaining Balance:    ${remaining_budget:.2f}")
