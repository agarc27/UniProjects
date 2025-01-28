# Andres Garcia Gomez
# ITP 259
# HW6
# Question 1

# Pre-Step: Import important modules
from keras.datasets import cifar100
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
pd.set_option('display.max_columns', None)

# This portion was used in order for the program to run on my laptop.
# Remove in case it messes up running the program.
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# Part 1
# Load the dataset.

(X_train, y_train), (X_test, y_test) = cifar100.load_data()

# Part 2
# Print the shapes of the training and testing data

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

# Part 3
# Visualize the first 30 images from the train dataset.

# Class names

class_names = ['apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle', 'bowl',
 'boy', 'bridge', 'bus', 'butterfly', 'camel', 'can', 'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee',
 'clock', 'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup', 'dinosaur', 'dolphin', 'elephant', 'flatfish',
 'forest', 'fox', 'girl', 'hamster', 'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard',
 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain', 'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid', 'otter',
 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine', 'possum', 'rabbit', 'raccoon',
 'ray', 'road', 'rocket', 'rose', 'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider',
 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor',
 'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm']

# Visualizing

plt.figure(figsize=[15, 10])
for i in range(30):
    plt.subplot(5, 6, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(X_train[i])
    plt.xlabel(class_names[y_train[i, 0]])
plt.show()

# Part 4
# Scale the train and test features

X_train = X_train/255
X_test = X_test/255

# Part 5
# Build a CNN Sequence of layers

model = Sequential()

model.add(Conv2D(50, kernel_size=(3, 3), strides=(1, 1),
                 padding='same', activation='relu', input_shape=(32, 32, 3)))
model.add(Conv2D(75, kernel_size=(3, 3), strides=(1, 1),
                 padding='same', activation='relu', input_shape=(32, 32, 3)))

model.add(MaxPool2D(pool_size=(2,2)))

model.add(Dropout(0.25))

model.add(Conv2D(100, kernel_size=(3, 3), strides=(1, 1),
                 padding='same', activation='relu', input_shape=(32, 32, 3)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(500, activation='relu'))
model.add(Dropout(0.40))
model.add(Dense(250, activation='relu'))
model.add(Dropout(0.3))

model.add(Dense(100, activation='softmax'))

# Part 6
# Show the summary of the model
model.summary()

# Part 7
# Use the loss function when compiling the model

model.compile(loss='sparse_categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

# Part 8
# Train the model with 20 epochs

fit = model.fit(X_train, y_train, batch_size=64, epochs=20, validation_data=(X_test, y_test))

# Part 9
# Plot the loss curve and accuracy curves.

# Loss
plt.figure(figsize=[6,4])
plt.plot(fit.history['loss'], 'black', linewidth=2.0)
plt.plot(fit.history['val_loss'], 'green', linewidth=2.0)
plt.legend(['Training Loss', 'Validation Loss'], fontsize=14)
plt.xlabel('Epochs', fontsize=10)
plt.ylabel('Loss', fontsize=10)
plt.title('Loss Curves', fontsize=12)

# Accuracy
plt.figure(figsize=[6,4])
plt.plot(fit.history['accuracy'], 'black', linewidth=2.0)
plt.plot(fit.history['val_accuracy'], 'blue', linewidth=2.0)
plt.legend(['Training Accuracy', 'Validation Accuracy'], fontsize=14)
plt.xlabel('Epochs', fontsize=10)
plt.ylabel('Accuracy', fontsize=10)
plt.title('Accuracy Curves', fontsize=12)

# Part 10
# Visualize the predicted and actual image labels for the first 30-images

# Predict
pred = model.predict(X_test)

# Convert predictions into label index
pred_classes = np.argmax(pred, axis=1)

# Plot images
plt.figure(figsize=[15,10])
for i in range(30):
    plt.subplot(5,6,i+1).imshow(X_test[i])
    plt.subplot(5,6,i+1).set_title('True: %s \nPredict: %s' %
                                   (class_names[y_test[i,0]],
                                    class_names[pred_classes[i]]))
    plt.subplot(5,6,i+1).axis('off')

plt.subplots_adjust(hspace=1)
plt.show()

# Part 11
# Visualize 30 random misclassified images in the test dataset.

failed_indices = []
for index in range(0, len(y_test)):
    if y_test[index, 0] != pred_classes[index]:
        failed_indices.append(index)

plt.figure(figsize=[15,10])
for i in range(30):
    plt.subplot(5, 6, i+1).imshow(X_test[random.choice(failed_indices)])
    plt.subplot(5, 6, i+1).set_title('True: %s \nPredict: %s' %
                                   (class_names[y_test[random.choice(failed_indices),0]],
                                    class_names[pred_classes[random.choice(failed_indices)]]))
    plt.subplot(5,6,i+1).axis('off')
    plt.xticks([])
    plt.yticks([])

plt.subplots_adjust(hspace=1)
plt.show()