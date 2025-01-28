# Andres Garcia Gomez
# ITP 259
# HW5
# Question 2

# Pre-Step: Load necessary modules and functions
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Part 1
# Read the handwritten data into a dataframe

myDF = pd.read_csv('A_Z_Handwritten_Data.csv')
# print(myDF.tail())

# Part 2
# Define the feature set and target variable

y = myDF['label']
X = myDF.drop(columns=['label'])

# Part 3
# Redefine the target such that the numbers in the target vector correspond to letters.

word_dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
             8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
             16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
             24:'Y', 25:'Z'}

y = y.map(word_dict)

# Part 4
# Print the shapes of the target and feature

print(X.shape)
print(y.shape)

# Part 5
# Show a countplot of the letters

sn.countplot(x=y, hue=y)
plt.show()

# Part 6
# Partition the data into train and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2024, stratify=y)

# Part 7
# Scale the data

X_train = X_train/255
X_test = X_test/255

# Part 8
# Create an MLPClassifier

model = MLPClassifier(hidden_layer_sizes=(100, 100, 100), max_iter=25, alpha=0.001,
                      learning_rate_init=0.01, random_state=2024)

# Part 9
# Fit the model to the training data

model.fit(X_train, y_train)

# Part 10
# Plot the loss curve.

plt.plot(model.loss_curve_)
plt.xlabel('Iteration')
plt.ylabel('Cross Entropy Loss')
plt.show()

# Part 11
# Print the accuracy of the test partition.

y_pred = model.predict(X_test)
print('Accuracy on the Test Set: ', metrics.accuracy_score(y_test, y_pred))

# Part 12
# Display the confusion matrix.

metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

# Part 13
# Display a correct letter prediction for the first result in the dataframe

X_testCorrect = X_test[y_test == y_pred]

imageData = X_testCorrect.iloc[0, :].values.reshape(28,28)
actualImageLabel = y_test[y_test == y_pred].iloc[0]
predictedImageLabel = y_test[y_test == y_pred].iloc[0]

plt.imshow(imageData, cmap='gray')
plt.title('Predicted Letter: ' + str(predictedImageLabel) + ' | ' +  'Actual Letter: ' + str(actualImageLabel))
plt.show()

# Part 14
# Display and incorrect letter prediction

X_testIncorrect = X_test[y_test != y_pred]
sample = X_testIncorrect.sample(n=1)
sampleIndex = sample.index
imageData = sample.values.reshape(28,28)
actualImageLabel1 = y_test[sampleIndex]
predictedImageLabel1 = model.predict(sample)

plt.imshow(imageData, cmap='gray')
plt.title('Predicted Letter: ' + str(predictedImageLabel1) + ' | ' +  'Actual Letter: ' + str(actualImageLabel1.values))
plt.show()
