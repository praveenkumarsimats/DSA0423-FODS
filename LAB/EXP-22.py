import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {
    "Age":[25,35,45,30,40],
    "Income":[30000,60000,80000,50000,70000],
    "BrowsingDuration":[5,15,20,10,18],
    "DeviceType":["Mobile","Desktop","Mobile","Tablet","Desktop"],
    "Purchase":["No","Yes","Yes","No","Yes"]
}

df = pd.DataFrame(data)

# Encoding categorical variables
le_device = LabelEncoder()
le_purchase = LabelEncoder()

df["DeviceType"] = le_device.fit_transform(df["DeviceType"])
df["Purchase"] = le_purchase.fit_transform(df["Purchase"])

# Features and target
X = df[["Age","Income","BrowsingDuration","DeviceType"]]
y = df["Purchase"]

# Train model
model = DecisionTreeClassifier()
model.fit(X,y)

# New customer data (use DataFrame)
new_customer = pd.DataFrame({
    "Age":[32],
    "Income":[55000],
    "BrowsingDuration":[12],
    "DeviceType":[le_device.transform(["Mobile"])[0]]
})

prediction = model.predict(new_customer)

print("Purchase Prediction:", le_purchase.inverse_transform(prediction))
