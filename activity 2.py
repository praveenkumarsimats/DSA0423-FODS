# ==========================================
# TechMart - Sales Data Analysis Challenge
# ==========================================

# 1️⃣ Import Required Libraries
import pandas as pd
import numpy as np

# 2️⃣ Load Dataset
df = pd.read_csv(r"C:\Users\rohan\Downloads\techmart_sales_input.csv")

# Convert OrderDate to datetime
df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# Preview Data
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# ==========================================
# 3️⃣ Handling Missing Data
# ==========================================

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing UnitPrice with median
median_price = df["UnitPrice"].median()
df["UnitPrice"] = df["UnitPrice"].fillna(median_price)

# Recalculate TotalSales after filling missing values
df["TotalSales"] = df["UnitsSold"] * df["UnitPrice"]

# ==========================================
# 4️⃣ Create New Features
# ==========================================

# Extract Month and Year
df["Month"] = df["OrderDate"].dt.month
df["Year"] = df["OrderDate"].dt.year

# Create Revenue Category Feature
df["RevenueCategory"] = np.where(df["TotalSales"] > 3000, 
                                 "High Revenue", 
                                 "Standard Revenue")

# ==========================================
# 5️⃣ Grouping and Aggregation
# ==========================================

# Total Sales by Region
sales_by_region = df.groupby("Region")["TotalSales"].sum().reset_index()
print("\nTotal Sales by Region:")
print(sales_by_region)

# Total Units Sold by Product Category
units_by_category = df.groupby("ProductCategory")["UnitsSold"].sum().reset_index()
print("\nUnits Sold by Product Category:")
print(units_by_category)

# Multi-level Grouping
summary = (
    df.groupby(["Region", "ProductCategory"])
      .agg(
          Total_Units_Sold=("UnitsSold", "sum"),
          Total_Revenue=("TotalSales", "sum"),
          Average_Unit_Price=("UnitPrice", "mean")
      )
      .reset_index()
)

print("\nGrouped Summary:")
print(summary)

# ==========================================
# 6️⃣ Pivot Table (Multi-Dimensional Analysis)
# ==========================================

pivot_table = pd.pivot_table(
    df,
    values="TotalSales",
    index="Region",
    columns="ProductCategory",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table - Revenue by Region and Category:")
print(pivot_table)

# ==========================================
# 7️⃣ Business Insights (Example Analysis)
# ==========================================

# Best performing region
best_region = sales_by_region.sort_values(by="TotalSales", ascending=False).iloc[0]
print(f"\nBest Performing Region: {best_region['Region']} "
      f"with revenue {best_region['TotalSales']}")

# Best selling category
best_category = units_by_category.sort_values(by="UnitsSold", ascending=False).iloc[0]
print(f"Best Selling Category: {best_category['ProductCategory']} "
      f"with {best_category['UnitsSold']} units sold")

# ==========================================
# 8️⃣ Export Processed Data
# ==========================================

summary.to_csv("techmart_sales_output_summary.csv", index=False)

print("\nAnalysis Complete. Output file saved.")
