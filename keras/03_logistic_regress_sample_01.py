#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

import matplotlib.pyplot as plt

# data set
x_data = np.array([-5, -4, -3, -2, -1, 0,1,2,3,4,5,6])
y_data = np.array([ 0,  0, 0,   0,  0, 0,0,1,1,1,1,1])

# model: linear regression input dense with dim =1
model = Sequential()
model.add(Dense(1, input_dim = 1, activation='sigmoid'))

# model compile:  SGD learning_rate of 0.01 
sgd = optimizers.SGD(learning_rate = 0.01)
model.compile(loss='binary_crossentropy', optimizer=sgd)

# model fit
history = model.fit(x_data, y_data, epochs=300, batch_size=1, shuffle=False)

loss_and_metric = model.evaluate(x_data, y_data, batch_size=1)
print ('Evaluate:\n', loss_and_metric)

# prediction
print ('Predict:\n', model.predict([7, -2, -3, 2, 1]))

# print model summary
print ('Model summary:\n')
model.summary()

# 학습 정확성 값과 검증 정확성 값을 플롯팅 합니다. 
# #print(history.history)
plt.plot(history.history['loss'])
plt.ylabel('Loss (binary_crossentropy)')
plt.xlabel('Epochs')
plt.savefig('03_tran_result.png')
#plt.show()
plt.clf()

plt.plot (x_data, model.predict(x_data), 'b', x_data, y_data, 'k.')
plt.show()
