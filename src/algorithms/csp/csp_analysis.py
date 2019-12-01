"""
Script to analyze the signal projected by the spatial filters generated by the CSP
"""
from src.data_preparation.data_preparation import load_csv, extract_single_trial
from src.signal_processing.signal_processing import bandpass_filter
from src.algorithms.csp.CSP import CSP

import matplotlib.pyplot as plt
import numpy as np

TIME_LENGTH = 750
TIME_WINDOW = 750

# Define the subject to analyze the data
subject = 4

# Read the data
left_data_file = f"data/bnci/by-subject/lefthand-subject-{subject}.csv"
right_data_file = f"data/bnci/by-subject/righthand-subject-{subject}.csv"

left_data = extract_single_trial(load_csv(left_data_file), TIME_LENGTH, TIME_WINDOW)
right_data = extract_single_trial(load_csv(right_data_file), TIME_LENGTH, TIME_WINDOW)

# Epoch the data
# left_data = epoch(left_data, 64)

# Bandpass filter the data
left_data = bandpass_filter(left_data)
right_data = bandpass_filter(right_data)

signal = np.concatenate((left_data[0, 0:750, :], right_data[0, 0:750, :]))

plt.figure(0)
plt.plot(signal[:, 0])
plt.show()

csp = CSP()
csp.fit([signal[0:750, :]], [signal[749:-1, :]])

s_p = csp.project(signal)

plt.figure(1)
plt.plot(signal[:, 0])
plt.show()

plt.figure(2)
plt.plot(signal[:, 1])
plt.show()