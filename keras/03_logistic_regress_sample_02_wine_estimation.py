#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

import matplotlib.pyplot as plt

# data set
df = pd.read_csv('./wine.csv')
x_data = df.values[:, 0:12]
y_data = df.values[:, 12]

print ('Wine quality samples:')
print (df)

# model: linear regression input dense with dim =1
model = Sequential()
model.add(Dense(1, input_dim = 12, activation='sigmoid'))

# model compile:  SGD learning_rate of 0.01 
sgd = optimizers.SGD(learning_rate = 0.01)
model.compile(loss='binary_crossentropy', optimizer=sgd)

# model fit
history = model.fit(x_data, y_data, epochs=100, batch_size=5, shuffle=False)

loss_and_metric = model.evaluate(x_data, y_data)
print ('Evaluate:\n', loss_and_metric)

# prediction
x_est0 = [7.1,0.39,0.35,12.5,0.044,26,72,0.9941,3.17,0.29,11.6,5]
x_est1 = [7.8,0.58,0.02,2,0.073,9,18,0.9968,3.36,0.57,9.5,7]
print ('Predict of sample 0 : %f' % (model.predict([x_est0])[0][0]) )
print ('Predict of sample 1 : %f' % (model.predict([x_est1])[0][0]) )

# print model summary
print ('Model summary:\n')
model.summary()

# 학습 정확성 값과 검증 정확성 값을 플롯팅 합니다. 
# #print(history.history)
plt.plot(history.history['loss'])
plt.ylabel('Loss (binary_crossentropy)')
plt.xlabel('Epochs')
plt.savefig('03_train_logistic_reg_wine.png')
#plt.show()
plt.clf()

# plt.plot (x_data, model.predict(x_data), 'b', x_data, y_data, 'k.')
# plt.show()
