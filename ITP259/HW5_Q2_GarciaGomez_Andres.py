# Andres Garcia Gomez
# ITP 259
# HW5
# Question 1

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
# Define the feature set and target variable. Redefine target with mapping.

y = myDF['label']
X = myDF.drop(columns=['label'])

word_dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
             8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
             16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
             24:'Y', 25:'Z'}
y = y.map(word_dict)

# Part 3
# Partition the data into train and test sets

X_trainLet, X_testLet, y_trainLet, y_testLet = train_test_split(X, y, test_size=1/7, random_state=2024, stratify=y)

# Part 4
# Scale the data

X_trainLet = X_trainLet/255
X_testLet = X_testLet/255

# Part 5
# Read the csv files into the dataframe.

trainDF = pd.read_csv('../Sample Final/mnist_train.csv')
testDF = pd.read_csv('../Sample Final/mnist_test.csv')

# Part 6
# Define train and test sets; map the target vector once again.

X_trainNum = trainDF.iloc[:, 1:]
y_trainNum = trainDF.iloc[:, 0]
X_testNum = testDF.iloc[:, 1:]
y_testNum = testDF.iloc[:, 0]

digit_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}

y_trainNum = y_trainNum.map(digit_dict)
y_testNum = y_testNum.map(digit_dict)

# Part 7
# Scale the data

X_trainNum = X_trainNum/255
X_testNum = X_testNum/255

# Part 8
# Concatenate the letter and number dataframes into one.

X_train = pd.concat([X_trainLet, X_trainNum], ignore_index=True)
X_test = pd.concat([X_testLet, X_testNum], ignore_index=True)
y_train = pd.concat([y_trainLet, y_trainNum], ignore_index=True)
y_test = pd.concat([y_testLet, y_testNum], ignore_index=True)

# Part 9
# Produce a countplot of the characters in the train set.
sn.countplot(x=y_train, hue=y_train, order=sorted(y_train.unique()))
plt.show()

# Part 10
# Create an MLPClassifier model.

model = MLPClassifier(hidden_layer_sizes=(100, 100, 100), max_iter=25, alpha=0.001,
                      learning_rate_init=0.01, random_state=2024)

# Part 11
# Fit the model to the training data

model.fit(X_train, y_train)

# Part 12
# Plot the loss curve.

plt.plot(model.loss_curve_)
plt.xlabel('Iteration')
plt.ylabel('Cross Entropy Loss')
plt.show()

# Part 13
# Print the accuracy of the test partition.

y_pred = model.predict(X_test)
print('Accuracy on the Test Set: ', metrics.accuracy_score(y_test, y_pred))

# Part 14
# Display the confusion matrix.

metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()

# Part 15
# Read the phrase of the given picture.

import matplotlib.image as mpimg
img = mpimg.imread('testPhrase.png')
r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]
imageData = 0.299*r + 0.587*g + 0.114*b
phrasePred = ''

for i in range(6):
    sample = imageData[:, 28*i:28*(i+1)]
    sampleData = sample.reshape(1, -1)
    sampleDF = pd.DataFrame(sampleData, columns=X_train.columns)
    modelPred = model.predict(sampleDF)
    phrasePred += str(modelPred[0])
    
plt.imshow(imageData, cmap='gray')
plt.title('Model Prediction: ' + phrasePred)
plt.show()