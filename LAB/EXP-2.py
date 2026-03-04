import pandas as pd

# Create DataFrame
order_data = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102],
    'order_date': ['2024-01-05', '2024-01-10', '2024-02-01', '2024-01-20', '2024-02-15'],
    'product_name': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Tablet'],
    'order_quantity': [1, 2, 1, 3, 2]
})

# Convert date column
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

# Total orders per customer
print("Total Orders:")
print(order_data.groupby('customer_id').size())

# Average quantity per product
print("\nAverage Quantity:")
print(order_data.groupby('product_name')['order_quantity'].mean())

# Earliest and latest dates
print("\nEarliest Date:", order_data['order_date'].min())
print("Latest Date:", order_data['order_date'].max())
