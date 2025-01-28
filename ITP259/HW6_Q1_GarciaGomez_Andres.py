# Andres Garcia Gomez
# ITP 259
# HW6
# Question 1

# Pre-Step: Import important modules
import keras.utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import tensorflow as tf

# This portion was used in order for the program to run on my laptop.
# Remove in case it messes up running the program.
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Step 1
# Set the random seed in order to reproduce results.

np.random.seed(2024)

# Step 2
# Load the dataset

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.fashion_mnist.load_data()

# Step 3
# Print the shapes of the train and test sets;

print(train_images.shape)
print(train_labels.shape)

print(test_images.shape)
print(test_labels.shape)

# Step 4
# Show a histogram in the train and test sets

apparel_dict = {0:'T-shirt/top', 1:'Trouser', 2:'Pullover', 3:'Dress', 4:'Coat', 5:'Sandal', 6:'Shirt', 7:'Sneaker', 8:'Bag', 9:'Ankle boot'}
train_label_names = pd.Series(train_labels).map(apparel_dict)
test_label_names = pd.Series(test_labels).map(apparel_dict)

fig, ax = plt.subplots(1,2)
sn.countplot(ax=ax[0], x=train_label_names, hue=train_label_names, order=sorted(train_label_names.unique()))
ax[0].set(title="Train Set")
ax[0].set(xlabel='')
ax[0].set_xticklabels(sorted(train_label_names.unique()), rotation=60)
sn.countplot(ax=ax[1], x=test_label_names, hue=test_label_names, order=sorted(test_label_names.unique()))
ax[1].set(title="Test Set")
ax[1].set(xlabel='')
ax[1].set_xticklabels(sorted(test_label_names.unique()), rotation=60)
plt.tight_layout()
plt.show()

# Step 5
# Scale the train and test features.

train_images = train_images/255
test_images = test_images/255

# Step 6
# Create five models.

model_1 = keras.Sequential()
model_1.add(keras.layers.Flatten(input_shape=(28, 28)))
model_1.add(keras.layers.Dense(10, activation='softmax'))


model_2 = keras.Sequential()
model_2.add(keras.layers.Flatten(input_shape=(28, 28)))
model_2.add(keras.layers.Dense(100, activation='relu'))
model_2.add(keras.layers.Dense(10, activation='softmax'))

model_3 = keras.Sequential()
model_3.add(keras.layers.Flatten(input_shape=(28, 28)))
model_3.add(keras.layers.Dense(100, activation='relu'))
model_3.add(keras.layers.Dense(100, activation='relu'))
model_3.add(keras.layers.Dense(10, activation='softmax'))

model_4 = keras.Sequential()
model_4.add(keras.layers.Flatten(input_shape=(28, 28)))
model_4.add(keras.layers.Dense(1000, activation='relu'))
model_4.add(keras.layers.Dense(10, activation='softmax'))

model_5 = keras.Sequential()
model_5.add(keras.layers.Flatten(input_shape=(28, 28)))
model_5.add(keras.layers.Dense(1000, activation='relu'))
model_5.add(keras.layers.Dense(1000, activation='relu'))
model_5.add(keras.layers.Dense(10, activation='softmax'))

# Part 7
# Print the summaries of all models.

model_1.summary()
model_2.summary()
model_3.summary()
model_4.summary()
model_5.summary()

# Part 8
# Set the model loss function and other things for each model

model_1.compile(loss='sparse_categorical_crossentropy', optimizer = 'sgd', metrics=['accuracy'])
model_2.compile(loss='sparse_categorical_crossentropy', optimizer = 'sgd', metrics=['accuracy'])
model_3.compile(loss='sparse_categorical_crossentropy', optimizer = 'sgd', metrics=['accuracy'])
model_4.compile(loss='sparse_categorical_crossentropy', optimizer = 'sgd', metrics=['accuracy'])
model_5.compile(loss='sparse_categorical_crossentropy', optimizer = 'sgd', metrics=['accuracy'])

# Part 9
# Fit to train the model and plot the loss curve.

# i. Fit model

fit_1 = model_1.fit(train_images, train_labels, epochs=50, verbose=0)
fit_2 = model_2.fit(train_images, train_labels, epochs=50, verbose=0)
fit_3 = model_3.fit(train_images, train_labels, epochs=50, verbose=0)
fit_4 = model_4.fit(train_images, train_labels, epochs=50, verbose=0)
fit_5 = model_5.fit(train_images, train_labels, epochs=50, verbose=0)

# ii. Plot the lost curve.

pd.DataFrame(fit_1.history).plot()
plt.title('Model 1')
plt.show()

pd.DataFrame(fit_2.history).plot()
plt.title('Model 2')
plt.show()

pd.DataFrame(fit_3.history).plot()
plt.title('Model 3')
plt.show()

pd.DataFrame(fit_4.history).plot()
plt.title('Model 4')
plt.show()

pd.DataFrame(fit_5.history).plot()
plt.title('Model 5')
plt.show()

# Part 9
# Display the accuracy of the tests.

print('Model 1')
model_1.evaluate(train_images, train_labels)
model_1.evaluate(test_images, test_labels)

print('Model 2')
model_2.evaluate(train_images, train_labels)
model_2.evaluate(test_images, test_labels)

print('Model 3')
model_3.evaluate(train_images, train_labels)
model_3.evaluate(test_images, test_labels)

print('Model 4')
model_4.evaluate(train_images, train_labels)
model_4.evaluate(test_images, test_labels)

print('Model 5')
model_5.evaluate(train_images, train_labels)
model_5.evaluate(test_images, test_labels)

# Part 11
# Which model to choose?

print('I would choose model 2 because it is less prone to overfitting - unlike models 4 and 5 with their large\n '
      'number of parameters to be optimized - while still maintaining a high accuracy on the test set, usurping models 1 and 3')

# Part 12
# Use selected model to predict the first item in the test dataset.

sample = test_images[0:1, :,:]
print(sample)
sampleLabel = pd.Series(test_labels[0]).map(apparel_dict)[0]
samplePredictedLabel = np.argmax(model_2.predict(sample), axis=1)
samplePredictedLabel = pd.Series(samplePredictedLabel).map(apparel_dict)[0]
correctPixelMatrix = sample.reshape(28,28)
plt.imshow(correctPixelMatrix, cmap='gray')
plt.title('Correct Label: ' + str(sampleLabel) + ' Predicted Label: ' + str(samplePredictedLabel))
plt.show()
