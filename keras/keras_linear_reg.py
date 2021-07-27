#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np

import tensorflow as tf
from tensorflow import keras

from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers

import matplotlib.pyplot as plt


# data set
x_data = np.array([1,2,3,4,5,6,])
y_data = np.array([10,20,30,40,50,60])

# model: linear regression input dense with dim =1
model = Sequential()
model.add(Dense(1, input_dim = 1, activation='linear'))

# model compile:  SGD learning_rate of 0.01 
sgd = optimizers.SGD(learning_rate = 0.01)
model.compile(loss='mse',optimizer=sgd, metrics=['accuracy'])

history = model.fit(x_data, y_data, epochs=10, shuffle=False, verbose=1)

# prediction
print (model.predict([7]))


# model summary
model.summary()

# 학습 정확성 값과 검증 정확성 값을 플롯팅 합니다. 
print(history.history)
plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Accuracy', 'Loss'], loc='upper left')
plt.savefig('tran_result.png')
plt.show()

