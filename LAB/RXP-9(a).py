import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20000, 25000, 22000, 27000, 30000]

# Create line plot
plt.plot(months, sales)
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
