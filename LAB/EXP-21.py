import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Sample dataset
data = {
    "Weight":[150,170,120,140,130,160],
    "Color":["Red","Orange","Yellow","Red","Yellow","Orange"],
    "Texture":["Smooth","Rough","Smooth","Smooth","Smooth","Rough"],
    "Type":["Apple","Orange","Banana","Apple","Banana","Orange"]
}

df = pd.DataFrame(data)

# Encoding categorical values
le_color = LabelEncoder()
le_texture = LabelEncoder()
le_type = LabelEncoder()

df["Color"] = le_color.fit_transform(df["Color"])
df["Texture"] = le_texture.fit_transform(df["Texture"])
df["Type"] = le_type.fit_transform(df["Type"])

# Features and target
X = df[["Weight","Color","Texture"]]
y = df["Type"]

# KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)

# Predict unknown fruit (use DataFrame)
new_data = pd.DataFrame([[145,0,1]], columns=["Weight","Color","Texture"])

prediction = model.predict(new_data)

print("Predicted Fruit Type:", le_type.inverse_transform(prediction))
N
