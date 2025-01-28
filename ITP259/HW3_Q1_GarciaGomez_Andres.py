# Andres Garcia Gomez
# ITP 259
# HW3
# Question 1

# Pre-Step: Import necessary modules and initial settings.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)

# Part 1
# Load the CSV file into Python and save as a DataFrame.

DF = pd.read_csv('insurance.csv')

# Part 2
# Creating a category plot in seaborn showcasing how sex and smoking impact medical costs.

# Format the subplots
sn.catplot(data=DF, x='sex', y='charges', col='smoker', kind='bar', hue='sex', errorbar=None)
plt.show()

# Part 3
# Creating a scatterplot using pandas showcasing how age and bmi impact medical costs.

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Subplot 1
ax[0].scatter(DF['age'], DF['charges'])
ax[0].set(xlabel='age')
ax[0].set(ylabel='charges')

# Subplot 2
ax[1].scatter(DF['bmi'], DF['charges'])
ax[1].set(xlabel='bmi')
ax[1].set(ylabel='charges')

fig.tight_layout()
plt.show()

# Part 4
# Define the feature and target vectors, with 'age', 'smoker', and 'bmi' in X and 'charges' in y.

# Target Vector
y = DF['charges']
# print(y.head())

# Feature Vector
X = DF[['age', 'bmi', 'smoker']]
# print(X.head())

# Part 5
# Convert the smoker column (categorical) into a dummy (numerical) feature

X_dummy = pd.get_dummies(data=X, columns=['smoker'], drop_first=True)
# print(X_dummy)

# Part 6
# We split the data for both the feature and target vector into test and training data.

X_train, X_test, y_train, y_test = train_test_split(X_dummy, y, test_size=0.3, random_state=2024)

# Part 7
# Fitting the data into our LinearRegression model

model = LinearRegression()
model.fit(X_train, y_train)

# Part 8
# Making predictions of y using our training data and then plotting the predicted and actual values

# Making predictions of y
y_pred = model.predict(X_test)

# Plotting the predictions against the actual
fig, ax = plt.subplots(1, 1, figsize=(7, 5))
ax.scatter(y_test, y_pred)
ax.set(xlabel='Actual Cost')
ax.set(ylabel='Predicted Cost')
fig.tight_layout()
plt.show()

# Part 9
# Display the score for the model of the test set

print('Model Score: ', model.score(X_test, y_test))
print()

# Part 10
# Using our model to predict the medical cost for someone with 'age' = 51, 'smoker_yes' = True, and 'bmi' = 21.

sampleData = np.array([[51, False, 29.1]])
sample = pd.DataFrame(data=sampleData, columns=X_dummy.columns)
print('Prediction of Medical Costs: ', model.predict(sample))

sampleData = np.array([[51, True, 29.1]])
sample = pd.DataFrame(data=sampleData, columns=X_dummy.columns)
print('Prediction of Medical Costs: ', model.predict(sample))
