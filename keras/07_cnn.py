#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import Callback

# Model 시각화하기 - https://codetorial.net/tensorflow/visualize_model.html
from tensorflow.keras.utils import plot_model

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------------------------------------------------
# full code: https://pinkwink.kr/1121
'''
# https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data
tf.keras.datasets.mnist.load_data
   x_train: uint8 NumPy array of grayscale image data with shapes (60000, 28, 28), containing the training data. Pixel values range from 0 to 255.
   y_train: uint8 NumPy array of digit labels (integers in range 0-9) with shape (60000,) for the training data.
   x_test: uint8 NumPy array of grayscale image data with shapes (10000, 28, 28), containing the test data. Pixel values range from 0 to 255.
   y_test: uint8 NumPy array of digit labels (integers in range 0-9) with shape (10000,) for the test data.

   x_train에는 총 60000개의 28×28 크기의 이미지가 담겨 있으며, y_train에는 이 x_train의 60000개에 대한 값(0~9)이 담겨 있는 레이블 데이터셋입니다. 
   그리고 x_train과 y_train은 각각 10000개의 이미지와 레이블 데이터셋입니다. 
   먼저 x_train와 y_train을 통해 모델을 학습하고 난 뒤에, x_test, y_test 를 이용해 학습된 모델의 정확도를 평가

'''

(x_train, y_train), (x_test, y_test) = mnist.load_data()
assert x_train.shape == (60000, 28, 28)
assert x_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)

# input image and dimension
img_rows = 28
img_cols = 28
input_shape = (28,28,1)

# reshape the data into a 4D tensor - (sample_number, x_img_size, y_img_size, num_channels)
# because the MNIST is greyscale, we only have a single channel - RGB colour images would have 3
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

# 0과 1사이로 scale
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)


# https://pinkwink.kr/1121, https://github.com/adventuresinML/adventures-in-ml-code
# Convolutional Neural Network 구성: convolution -> pooling -> flatten 
model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1), padding='same',  activation='relu',  input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (2, 2), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))


# print model summary & plot_model () - https://codetorial.net/tensorflow/visualize_model.html
model.summary()
plot_model(model, to_file='07_cnn_model_shapes.png', show_shapes=True)


# model compile & fit
batch_size = 128
epochs = 12

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history=model.fit(x_train, y_train,
            batch_size=batch_size,
            epochs=epochs,
            verbose=1, 
            validation_data=(x_test, y_test) )

# model evaluate
score = model.evaluate(x_test, y_test, verbose=1)
title = 'Test loss: %s, Test accuracy: %s' % (score[0], score[1])
print('Test loss:', score[0])
print('Test accuracy:', score[1])


#plt.plot(range(1, epochs), history.acc)
plt.plot(history.history['loss'])
plt.plot(history.history['accuracy'])
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title(title)
plt.show()
plt.savefig('07_cnn_mnist_accuracy.png')
plt.clf()


# predict - single image
n = 1
predicted_result = model.predict(x_test[n].reshape((1, 28, 28, 1)))
predicted_labels = np.argmax(predicted_result, axis=1)
print('The Answer is ', predicted_labels)
plt.imshow(x_test[n].reshape(28, 28), cmap='Greys', interpolation='nearest')
plt.show()

# predict - random choice
import random
predicted_result = model.predict(x_test)
predicted_labels = np.argmax(predicted_result, axis=1)
test_labels = np.argmax(y_test, axis=1)

wrong_result = []
for n in range(0, len(test_labels)):
    if predicted_labels[n] != test_labels[n]:
        wrong_result.append(n)
print ('# of bad prediction:', len(wrong_result))

samples = random.choices(population=wrong_result, k=16)

count = 0
nrows = ncols = 4

plt.figure(figsize=(12,8))
for n in samples:
    count += 1
    plt.subplot(nrows, ncols, count)
    plt.imshow(x_test[n].reshape(28, 28), cmap='Greys', interpolation='nearest')
    tmp = "Label:" + str(test_labels[n]) + ", Prediction:" + str(predicted_labels[n])
    plt.title(tmp)

plt.tight_layout()
plt.savefig('07_cnn_mnist_wrong_prediction.png')
plt.show()