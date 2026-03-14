import numpy as np
import matplotlib.pyplot as plt

# Sample data
temperature = np.array([30,32,35,28,26,31,33])
rainfall = np.array([5,3,2,6,7,4,3])

# Calculate correlation coefficient
correlation = np.corrcoef(temperature, rainfall)

print("Correlation Coefficient:", correlation[0][1])

# Scatter plot
plt.scatter(temperature, rainfall)

plt.xlabel("Temperature")
plt.ylabel("Rainfall")
plt.title("Temperature vs Rainfall")

plt.show()
