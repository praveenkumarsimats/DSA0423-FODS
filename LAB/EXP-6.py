import numpy as np

# Time intervals (in seconds)
time = np.array([0, 1, 2, 3, 4])

# Vertical positions (in meters)
position = np.array([0, 10, 15, 10, 0])

# Calculate average velocity
change_in_position = position[-1] - position[0]
change_in_time = time[-1] - time[0]

average_velocity = change_in_position / change_in_time

print("Average Velocity:", average_velocity, "m/s")
