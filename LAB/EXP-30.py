import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("shoe_sales.csv")

# Calculate frequency distribution
frequency = data.groupby("shoe_size")["quantity"].sum()

# Display frequency table
print("Frequency Distribution of Shoe Sizes:\n")
print(frequency)

# Bar chart
frequency.plot(kind="bar")

plt.xlabel("Shoe Size")
plt.ylabel("Quantity Sold")
plt.title("Frequency Distribution of Shoe Sizes")
plt.show()
