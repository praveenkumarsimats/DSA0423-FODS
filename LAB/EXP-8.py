import numpy as np

# NumPy array containing product prices (in rupees)
sales_data = np.array([500, 1200, 750, 900, 1500, 650, 1100])

# Calculate average price
average_price = np.mean(sales_data)

print("Average Price of Products Sold:", average_price)
