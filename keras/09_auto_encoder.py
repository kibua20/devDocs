#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf
from tensorflow.keras import datasets
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import UpSampling2D

# 데이터 불러오기
(X_tn0,y_tn0),(X_te0,y_te0)=datasets.mnist.load_data()

# 원본 데이터 차원 확인
print(X_tn0.shape)
print(y_tn0.shape)
print(X_te0.shape)
print(y_te0.shape)

# 원본 데이터 시각화
plt.figure(figsize=(10, 5))
for i in range(2*5):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_tn0[i].reshape((28, 28)), cmap='Greys')
#plt.show()
plt.savefig('09_autoencoder_original_data.png')


# 피쳐 데이터 스케일 조정
X_tn_re = X_tn0.reshape(60000,28,28,1)
X_tn = X_tn_re/255
print(X_tn.shape)

X_te_re = X_te0.reshape(10000,28,28,1)
X_te = X_te_re/255
print(X_te.shape)

# 노이즈 피쳐 데이터 
X_tn_noise = X_tn + np.random.uniform(-1,1,size=X_tn.shape)
X_te_noise = X_te + np.random.uniform(-1,1,size=X_te.shape)

# 노이즈 데이터 스케일링: 0~1 값
X_tn_ns = np.clip(X_tn_noise, a_min=0, a_max=1)
X_te_ns  = np.clip(X_te_noise, a_min=0, a_max=1)

# 노이즈 데이터 시각화
plt.figure(figsize=(10, 5))
for i in range(2*5):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_tn_ns[i].reshape((28, 28)), cmap='Greys')
#plt.show()
plt.savefig('09_autoencoder_noise_data.png')

# 오토인코더
model = Sequential()
# 인코딩
model.add(Conv2D(20, kernel_size=(5,5), input_shape=(28,28,1), padding='same',  activation='relu'))
model.add(MaxPool2D(pool_size=2,  padding='same'))

# 디코딩
model.add(Conv2D(10, kernel_size=(5,5),  padding='same',   activation='relu'))
model.add(UpSampling2D())
model.add(Conv2D(1, kernel_size=(5,5),   padding='same',   activation='relu'))

# 모형 컴파일
# 오토인코더의 손실은 MNIST의 28 X 28 이미지 각각의 pixel 값에 대하여 원본 - 디코딩된 이미지 간의 MSE 오차를 적용하여 학습
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])

# 학습 - 학습데이터 또한, 원본이미지를 그대로 label 이미지로 활용합니다. 왜냐하면, Input Data와 Output Data 간의 차이를 줄이는데에 모델의 성능
hist = model.fit(X_tn_ns, X_tn, epochs=1, batch_size=100)

# 예측값
X_pred = model.predict(X_tn_ns)

# 오토인코딩 데이터 시각화
plt.figure(figsize=(10, 5))
for i in range(2*5):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_pred[i].reshape((28, 28)), cmap='Greys')
#plt.show()
plt.savefig('09_autoencoder_predict.png')

# https://teddylee777.github.io/tensorflow/autoencoder
# 오토인코더는 고차원의 정보를 압축해 주는 인코더와 압축된 정보를 다시 원래 정보로 돌려주는 디코더로 이루어져 있습니다.
# 오토인코더 모델은 인코더 - 디코더의 결합된 형태로 만들어집니다.
# 나중에 디코더만 따로 떼네어, 압축된 정보를 입력으로 주게 되면, 알아서 원본 이미지와 유사한 마치 Fake 이미지를 만들어 주도록 유도할 수도 있습니다

