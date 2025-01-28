# Andres Garcia Gomez
# ITP 259
# HW4
# Question 1

# Pre-Step: Load necessary modules and functions
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Part 1
# Generate the data as described in the document.

np.random.seed(2024)
n = 1000
theta = 2*np.pi*np.random.random([n, 1])
label = np.random.randint(0, 2, n).reshape(n, 1)
r = (2*theta + np.pi)*(-1)**label


myDF = pd.DataFrame(label, columns=['Label'])
myDF['X1'] = r*np.cos(theta) + np.random.randn(n, 1)
myDF['X2'] = r*np.sin(theta) + np.random.randn(n, 1)

# Part 2
# Create a scatterplot of the data we just created.
sn.scatterplot(data=myDF, x='X1', y='X2', hue='Label', legend=False)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spiral Distribution')
plt.show()

# Part 3
# Define feature and target vectors; partition the dataset.

y = myDF['Label']
print(y)
X = myDF.drop(columns=['Label'])
print(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.70, random_state=2024, stratify=y)

# Part 4
# Train the MLPClassifier using your own parameters

model = MLPClassifier(hidden_layer_sizes=(5, 2), activation='tanh', alpha=0.001, learning_rate_init=0.01, verbose=True)
model.fit(X_train, y_train)

# Part 5
# Plot the loss curve.

plt.plot(model.loss_curve_)
plt.xlabel('Iteration')
plt.ylabel('Cross Entropy Loss')
plt.show()

# Part 6
# Print the accuracy of the test partition.

y_pred = model.predict(X_test)
print('Accuracy on the Test Set: ', metrics.accuracy_score(y_test, y_pred))

# Part 7
# Display the confusion matrix.

metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

# Part 8
# Create the decision boundary.

X1 = np.arange(-20, 20, 0.1)
X2 = np.arange(-20, 20, 0.1)
meshSize = len(X1)*len(X2)

X1, X2 = np.meshgrid(X1, X2)
X_decision = pd.DataFrame({'X1':np.reshape(X1, meshSize), 'X2':np.reshape(X2, meshSize)})
Z = model.predict(X_decision)

plt.scatter(X_decision['X1'], X_decision['X2'], c=Z, cmap='cool')
plt.scatter(myDF['X1'], myDF['X2'], marker='.', c=y, cmap='RdBu')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Decision Boundary')
plt.show()
