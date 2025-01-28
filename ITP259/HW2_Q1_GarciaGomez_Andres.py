# Andres Garcia Gomez
# ITP 259
# HW2
# Question 1

# Pre-Step: Import necessary modules
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Defining our variables as empty lists that we'll later fit with many integers
X = []
Y = []

# Step 2: Iterate through these variables to fill them with integers as desired.

# This loop generates 200 random numbers that are appended into X and Y
for h in range(200):
    X.append(np.random.randint(1, 200))
    Y.append(np.random.randint(1, 200))

# Step 3: Plotting our values using matplotlib scatter function

plt.scatter(X, Y, c='r', s=12)
plt.xlabel('Random Integer', c='b')
plt.ylabel('Random Integer', c='b')
plt.title('Scatter of random integers', c='g')
plt.show()
