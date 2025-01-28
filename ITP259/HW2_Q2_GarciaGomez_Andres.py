# Andres Garcia Gomez
# ITP 259
# HW2
# Question 2

# Pre-Step: Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Store the (already modified) data into a DataFrame

DF = pd.read_csv('data.csv')
# print(DF.head(10))

# Step 2: Create the variables we want to plot from the DataFrame
X = DF['Year']
Y = DF['Value']

# Step 3: Plot the data using matplotlib
plt.plot(X, Y, c='r', marker='o', linestyle='dashed' )
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly')
plt.title('Global Temperature')
plt.show()
