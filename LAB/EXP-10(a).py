import matplotlib.pyplot as plt

# Monthly data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
temperature = [22, 25, 28, 32, 35, 30]

# Create line plot
plt.plot(months, temperature)
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.show()
