import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample car dataset
data = {
    "Speed": [120, 150, 100, 130, 170],
    "Mileage": [15, 12, 18, 14, 10],
    "Horsepower": [110, 150, 90, 130, 170],
    "Weight": [1000, 1200, 900, 1100, 1400]
}

df = pd.DataFrame(data)

# Multivariate Scatter Plot
sns.scatterplot(x="Speed", y="Mileage", size="Horsepower", hue="Weight", data=df)
plt.title("Multivariate Scatter Plot")
plt.show()

# Scatter Plot Matrix
sns.pairplot(df)
plt.show()
