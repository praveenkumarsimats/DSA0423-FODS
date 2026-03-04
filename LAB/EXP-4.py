import pandas as pd

# Create DataFrame
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Chennai', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai'],
    'bedrooms': [3, 5, 4, 6, 2],
    'area_sqft': [1200, 2500, 1500, 3000, 1000],
    'listing_price': [5000000, 12000000, 6500000, 15000000, 4500000]
})

# 1. Average listing price by location
print("Average Price by Location:")
print(property_data.groupby('location')['listing_price'].mean())

# 2. Properties with more than 4 bedrooms
count = len(property_data[property_data['bedrooms'] > 4])
print("\nProperties with more than 4 bedrooms:", count)

# 3. Property with largest area
largest = property_data.loc[property_data['area_sqft'].idxmax()]
print("\nProperty with Largest Area:")
print(largest)
