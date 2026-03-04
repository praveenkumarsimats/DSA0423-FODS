import numpy as np

# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1200, 5000000],
    [5, 2500, 12000000],
    [4, 1500, 6500000],
    [6, 3000, 15000000],
    [2, 1000, 4500000]
])

# Filter houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price (3rd column index = 2)
average_price = np.mean(filtered_houses[:, 2])

print("Average Sale Price of Houses with More Than 4 Bedrooms:", average_price)
