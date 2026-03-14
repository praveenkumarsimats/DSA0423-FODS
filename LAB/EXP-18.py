import pandas as pd
import numpy as np

# Sample temperature dataset
data = {
    "City": ["CityA","CityB","CityC"],
    "Day1":[30,25,28],
    "Day2":[32,27,29],
    "Day3":[31,26,30],
    "Day4":[33,28,31]
}

df = pd.DataFrame(data)

# Set city as index
df.set_index("City", inplace=True)

# Mean temperature
mean_temp = df.mean(axis=1)

# Standard deviation
std_temp = df.std(axis=1)

# Temperature range
temp_range = df.max(axis=1) - df.min(axis=1)

print("Mean Temperature:")
print(mean_temp)

print("\nStandard Deviation:")
print(std_temp)

# City with highest range
print("\nCity with Highest Temperature Range:", temp_range.idxmax())

# City with most consistent temperature
print("City with Most Consistent Temperature:", std_temp.idxmin())
