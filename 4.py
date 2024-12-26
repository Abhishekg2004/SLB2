import numpy as np
from scipy import stats

data_input = input("Enter the data values separated by commas (e.g., 10, 20, 30): ")
frequencies_input = input("Enter the corresponding frequencies separated by commas (e.g., 2, 3, 4): ")
    
data = list(map(int, data_input.split(',')))
freq = list(map(int, frequencies_input.split(',')))

expanded_data = np.repeat(data, freq)

mean = np.mean(expanded_data)
print(f"Mean: {mean:.2f}")

median = np.median(expanded_data)
print(f"Median: {median}")

mode = stats.mode(expanded_data)
print(f"Mode: {mode[0]} ")

std_dev = np.std(expanded_data)
print(f"Standard Deviation: {std_dev:.2f}")

variance = np.var(expanded_data)
print(f"Variance: {variance:.2f}")

mean_deviation = np.mean(np.abs(expanded_data - mean))
print(f"Mean Deviation: {mean_deviation:.2f}")

q1 = np.percentile(expanded_data, 25)
q3 = np.percentile(expanded_data, 75)
quartile_deviation = (q3 - q1) / 2
print(f"Quartile Deviation: {quartile_deviation}")