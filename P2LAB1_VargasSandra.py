# Sandra Vargas
# February 27, 2024
# Driving Costs Calculator
# This Python program calculates the cost of driving for miles based on the car's gas mileage and the cost of gas provided by the user.

def calculate_gas_cost(miles_per_gallon, cost_per_gallon):
    cost_20_miles = 20 / miles_per_gallon * cost_per_gallon
    cost_75_miles = 75 / miles_per_gallon * cost_per_gallon
    cost_500_miles = 500 / miles_per_gallon * cost_per_gallon
    return cost_20_miles, cost_75_miles, cost_500_miles

# Input
miles_per_gallon = float(input("Enter the car's gas mileage (miles/gallon): "))
cost_per_gallon = float(input("Enter the cost of gas (dollars/gallon): "))

# Calculate gas cost
cost_20_miles, cost_75_miles, cost_500_miles = calculate_gas_cost(miles_per_gallon, cost_per_gallon)

# Output
print(f'The gas cost for driving 20 miles is: ${cost_20_miles:.2f}')
print(f'The gas cost for driving 75 miles is: ${cost_75_miles:.2f}')
print(f'The gas cost for driving 500 miles is: ${cost_500_miles:.2f}')
