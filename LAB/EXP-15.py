import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Sample clinical trial data
control = [50, 55, 52, 58, 54]
treatment = [65, 70, 68, 72, 66]

# Perform hypothesis testing (t-test)
t_stat, p_value = ttest_ind(control, treatment)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Check significance
if p_value < 0.05:
    print("The treatment has a statistically significant effect.")
else:
    print("The treatment does NOT have a statistically significant effect.")

# Calculate mean values
means = [np.mean(control), np.mean(treatment)]
groups = ["Control", "Treatment"]

# Plot graph
plt.bar(groups, means)
plt.xlabel("Groups")
plt.ylabel("Average Value")
plt.title("Control vs Treatment Group Comparison")
plt.show()
