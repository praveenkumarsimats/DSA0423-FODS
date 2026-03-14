import pandas as pd

# Sample sales data
sales_data = pd.DataFrame({
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile',
                'Headphones', 'Tablet', 'Laptop', 'Camera', 'Mobile'],
    'Quantity': [5, 10, 7, 3, 6, 8, 4, 2, 9, 5]
})

# Group by Product and calculate total quantity sold
total_sales = sales_data.groupby('Product')['Quantity'].sum()

# Sort in descending order and get top 5
top_5 = total_sales.sort_values(ascending=False).head(5)

print("Top 5 Most Sold Products:")
print(top_5)
