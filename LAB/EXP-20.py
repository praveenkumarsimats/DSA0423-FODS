import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv(r"C:\Users\reddy\OneDrive\Desktop\EXPERIMENTS\players.csv")

# Top 5 players with highest goals
top_goals = df.sort_values(by="Goals", ascending=False).head(5)
print("Top 5 Players with Highest Goals:")
print(top_goals[["Name","Goals"]])

# Top 5 players with highest salary
top_salary = df.sort_values(by="Salary", ascending=False).head(5)
print("\nTop 5 Players with Highest Salary:")
print(top_salary[["Name","Salary"]])

# Average age
avg_age = df["Age"].mean()
print("\nAverage Age of Players:", avg_age)

# Players above average age
print("\nPlayers above Average Age:")
print(df[df["Age"] > avg_age][["Name","Age"]])

# Visualization of player positions
position_count = df["Position"].value_counts()
position_count.plot(kind="bar")

plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.title("Distribution of Players by Position")
plt.show()
