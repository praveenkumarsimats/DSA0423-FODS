import numpy as np

# 4x4 matrix (Rows: Students, Columns: Math, Science, English, History)
student_scores = np.array([
    [85, 78, 90, 88],
    [92, 81, 76, 85],
    [88, 79, 84, 80],
    [75, 85, 89, 92]
])

subjects = ["Math", "Science", "English", "History"]

# Calculate average for each subject
average_scores = np.mean(student_scores, axis=0)

# Find subject with highest average
highest_subject = subjects[np.argmax(average_scores)]

print("Average Scores:", average_scores)
print("Subject with Highest Average:", highest_subject)
