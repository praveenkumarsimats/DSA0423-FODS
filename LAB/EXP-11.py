import numpy as np

# Fuel efficiency data (in miles per gallon)
fuel_efficiency = np.array([20, 25, 30, 28, 35])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Compare two car models (example: model 1 and model 3)
old_model = fuel_efficiency[0]   # 20 mpg
new_model = fuel_efficiency[2]   # 30 mpg

# Calculate percentage improvement
percentage_improvement = ((new_model - old_model) / old_model) * 100

print("Average Fuel Efficiency:", average_efficiency, "mpg")
print("Percentage Improvement:", percentage_improvement, "%")
