# Program that generates a plot of a normally distributed set of 1000 values
# and plots the function h(x)=x**3
# Author: Tom Brophy
# Information on generating a normal distribution found here: 
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# Assumption for x**3 function is that range is inclusive of 0 and 10


import numpy as np
import matplotlib.pyplot as plt

# Set values at the start
mean_val = 5
std_dev = 2
num_vals = 1000
np.random.seed(31) # Some experimenting with seed vals and this was closest to keeping within 0 and 10 I could find.

# Create values to populate the histogram
hist_vals = np.random.normal(mean_val, std_dev, num_vals)

# Create values for x**3 plot
xpoints = np.array(range(0, 11))
ypoints = xpoints*xpoints*xpoints

# Create and label plots
plt.hist(hist_vals, label='Histogram')
plt.plot(xpoints, ypoints, label='X cubed')
plt.title('Week 08 Task - Plotting')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.show()
