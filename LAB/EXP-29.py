import pandas as pd
import numpy as np
from scipy import stats

# Load dataset
data = pd.read_csv("customer_reviews.csv")

# Extract ratings column
ratings = data["rating"]

# Confidence level
confidence = 0.95

# Calculate statistics
mean_rating = np.mean(ratings)
std_error = stats.sem(ratings)

# Calculate confidence interval
confidence_interval = stats.t.interval(confidence, len(ratings)-1, loc=mean_rating, scale=std_error)

print("Average Rating:", mean_rating)
print("95% Confidence Interval:", confidence_interval)
