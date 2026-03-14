import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = {
'Age':[25,30,45,50,35,40],
'BP':[120,130,140,150,125,135],
'Cholesterol':[180,200,220,240,190,210],
'Outcome':['Good','Good','Bad','Bad','Good','Bad']
}

df = pd.DataFrame(data)

df['Outcome'] = df['Outcome'].map({'Good':1,'Bad':0})

X = df[['Age','BP','Cholesterol']]
y = df['Outcome']

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.3,stratify=y,random_state=42)

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Accuracy:",accuracy_score(y_test,y_pred))
print("Precision:",precision_score(y_test,y_pred,zero_division=0))
print("Recall:",recall_score(y_test,y_pred,zero_division=0))
print("F1 Score:",f1_score(y_test,y_pred,zero_division=0))
