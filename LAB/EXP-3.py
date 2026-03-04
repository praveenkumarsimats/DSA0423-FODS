import pandas as pd

# Create DataFrame
sales_data = pd.DataFrame({
    'Product': ['Laptop', 'Mobile', 'Tablet'],
    'Price': [50000, 20000, 15000],
    'Quantity': [2, 3, 4]
})

# Calculate Total Sales
sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

# Display result
print(sales_data)
