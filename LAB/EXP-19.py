import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample dataset
data = {
    "CustomerID":[1,2,3,4,5,6],
    "AmountSpent":[200,500,150,800,120,700],
    "ItemsPurchased":[5,8,3,10,2,9]
}

df = pd.DataFrame(data)

# Select features
X = df[["AmountSpent","ItemsPurchased"]]

# Apply K-Means
kmeans = KMeans(n_clusters=2)
df["Cluster"] = kmeans.fit_predict(X)

print(df)

# Visualization
plt.scatter(df["AmountSpent"], df["ItemsPurchased"], c=df["Cluster"])
plt.xlabel("Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Segmentation using K-Means")
plt.show()
