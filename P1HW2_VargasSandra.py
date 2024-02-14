# Sandra Vargas
# 2024-02-14
# P1HW2: Travel Budget Calculator
# Calculates the remaining budget for a trip


# Get user input
budget = float(input("Enter your total travel budget (in dollars): "))
destination = input("Enter your travel destination): ")
gasoline_cost = float(input("How much do you think you will spend on gas: "))
hotel_cost = float(input("Approximately, How much do you think you will spend on accommodation: "))
food_cost = float(input("How much do you think you will spend on food: "))
train_cost = float(input("How much do you think you will spend on train tickets: "))
flight_cost = float(input("How much do you think you will spend on flights: "))
souvenirs_cost = float(input("How much do you think you will spend on souvenirs: "))
activities_cost = float(input("Last, how much do you think you will spend on activities: "))

# Calculate total expenses and remaining budget
total_expenses = gasoline_cost + hotel_cost + food_cost + train_cost + flight_cost + souvenirs_cost + activities_cost
remaining_budget = budget - total_expenses

# Print results
print("# Travel Expenses:")
print("Destination:", destination)
print("Initial budget:", budget, "dollars")
print("Total expenses:", total_expenses, "dollars")
print("Remaining budget:", remaining_budget, "dollars")
