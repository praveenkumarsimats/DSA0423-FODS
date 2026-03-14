import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {
    "Income":[30000,50000,70000,40000,60000],
    "CreditScore":[600,700,750,650,720],
    "DebtRatio":[0.4,0.3,0.2,0.5,0.25],
    "EmploymentYears":[2,5,7,3,6],
    "Risk":["High","Low","Low","High","Low"]
}

df = pd.DataFrame(data)

# Encode target variable
le = LabelEncoder()
df["Risk"] = le.fit_transform(df["Risk"])

# Features and target
X = df[["Income","CreditScore","DebtRatio","EmploymentYears"]]
y = df["Risk"]

# Decision Tree Model
model = DecisionTreeClassifier(random_state=0)
model.fit(X,y)

# New applicant data (use DataFrame)
new_data = pd.DataFrame({
    "Income":[45000],
    "CreditScore":[680],
    "DebtRatio":[0.35],
    "EmploymentYears":[4]
})

prediction = model.predict(new_data)

print("Predicted Credit Risk:", le.inverse_transform(prediction))
