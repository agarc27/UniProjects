# Andres Garcia Gomez
# ITP 259
# HW3
# Question 2

# Pre-Step: Import necessary modules and initial settings.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Part 1
# Load the CSV file into Python and save as a DataFrame.

DF = pd.read_csv('titanic.csv')

# Part 2
# Ensure that there are no missing values using the isnull function and the sum function.

print(DF.isnull().sum())
print()

# Part 3
# Drop the Passenger column using the drop function

# print(DF.columns)
# print()
DF = DF.drop(columns='Passenger')
# print(DF.columns)

# Part 4
# Creating count plots for each of the remaining attributes.

fig, axes = plt.subplots(2, 2, figsize=(16, 9))
sn.countplot(data=DF, x='Class', ax=axes[0,0]) # Count plot for Class
sn.countplot(data=DF, x='Sex', ax=axes[0,1]) # Count plot for Sex
sn.countplot(data=DF, x='Age', ax=axes[1,0]) # Count plot for Age
sn.countplot(data=DF, x='Survived', ax=axes[1,1]) # Count plot for Survived

# Tidying up the Figure
fig.suptitle('Count Plots for All Attributes')
fig.tight_layout()
plt.show()

# Part 5
# Convert the categorical variables (all but Survived) into dummy variables.

# Make the feature and target vectors now as it'll be easier for when we convert the variables.
y = DF['Survived']
X = DF.drop(columns='Survived')

# Converting the variables into dummies.
X = pd.get_dummies(X, columns = ['Class', 'Sex', 'Age'], drop_first=True)
# print(X)

# Part 6
# Split the data into testing and training sets.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2024)

# Part 7
# Fitting the training data into the model.

model = LogisticRegression()
model.fit(X_train, y_train)

# Part 8
# Display the accuracy of the model on predicting survivability.

y_pred = model.predict(X_test)
print('Accuracy on the Test Set: ', metrics.accuracy_score(y_test, y_pred))

# Part 9
# Displaying the confusion matrix for the model.

metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=['Yes', 'No'])
plt.show()

# Part 10
# Predict the survivability of a 2nd Class Female Adult Passenger.
sampleData = np.array([[True, False, False, False, False]])
sample = pd.DataFrame(data=sampleData, columns=X.columns)
print('Prediction of Survivability: ', model.predict(sample))