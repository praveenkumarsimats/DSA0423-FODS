import numpy as np
from scipy import stats

# Sample revenue data from 100 customers (example values)
revenue = np.random.normal(200, 50, 100)   # mean=200, std=50, sample size=100

# Confidence level
confidence = 0.95

# Sample statistics
mean_revenue = np.mean(revenue)
std_error = stats.sem(revenue)

# Confidence interval calculation
confidence_interval = stats.t.interval(confidence, len(revenue)-1, loc=mean_revenue, scale=std_error)

print("Mean Revenue:", mean_revenue)
print("95% Confidence Interval:", confidence_interval)
