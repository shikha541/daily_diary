# day 8 [19 June 2024]
 # Descriptive Statistics
# Calculate the mean, median, mode, and standard deviation of the data.
#1 mean: average of numbers
import numpy as np
data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
#2 median: middle value in sorted list of numbers
data = np.array([1, 2, 3, 4, 5])
median = np.median(data)
#3 mode: 
data = np.array([1, 2, 2, 3, 4,5])
mode = np.bincount(data).argmax()



import statistics

# Sample dataset
data = [4, 8, 15, 16, 23, 42, 16]

# Calculate Mean
mean_value = statistics.mean(data)
print("Mean:", mean_value)

# Calculate Median
median_value = statistics.median(data)
print("Median:", median_value)

# Calculate Mode
try:
    mode_value = statistics.mode(data)
    print("Mode:", mode_value)
except statistics.StatisticsError:
    print("No unique mode found")


import pandas as pd

# Sample dataset
data = [4, 8, 15, 16, 23, 42, 16]

# Create a Pandas Series
s = pd.Series(data)

# Calculate Mean
mean_value = s.mean()
print("Mean:", mean_value)

# Calculate Median
median_value = s.median()
print("Median:", median_value)

# Calculate Mode
mode_value = s.mode()
print("Mode:", mode_value)
