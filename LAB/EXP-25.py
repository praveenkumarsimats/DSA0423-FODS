import numpy as np

# Population dataset
data = np.array([10,12,15,18,20,22,25,28,30,35])

# Random sampling
sample = np.random.choice(data, size=5)

print("Sample Data:", sample)

# Mean estimation
mean_est = np.mean(sample)

# Variance estimation
var_est = np.var(sample)

print("Estimated Mean:", mean_est)
print("Estimated Variance:", var_est)
