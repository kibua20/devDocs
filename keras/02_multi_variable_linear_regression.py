#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
# from keras.models import Sequential
# from keras.layers import Dense
# from keras import optimizers

import matplotlib.pyplot as plt

# data set
x_data = np.array([
                    [73,80,75],
                    [93,88,93],
                    [89,91,90],
                    [80,80,80],
                    [96,98,100],
                    [73,66,70],
                  ])
y_data = np.array([72,88,92,81,100,71])

# model: linear regression input dense with dim =1
model = Sequential()

# 다중 회귀에서는 input dim 값과, output_dim 값을 변경해야 함.
model.add(Dense(1, input_dim = 3, activation='linear'))

# model compile:  SGD learning_rate of 0.01 
sgd = optimizers.SGD(learning_rate = 0.00001)
model.compile(loss='mse', optimizer=sgd, metrics=['mse'])

# model fit
history = model.fit(x_data, y_data, batch_size=1, epochs=100, shuffle=False, verbose=1)

# prediction
x_test = np.array([[90,88,93], [70,70,70]])
print (model.predict(x_test))

# print model summary
model.summary()

# 학습 정확성 값과 검증 정확성 값을 플롯팅 합니다. 
# print(history.history)
#plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('Train Loss')
plt.ylabel('Loss')
plt.savefig('tran_result.png')

