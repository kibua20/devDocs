#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

def test_onehot_encode():
    x = np.array(['dog', 'cat', 'bird', 'fish'])

    # label encoder :  text를 숫자로 인코딩
    encoder = LabelEncoder()
    encoder.fit(x)
    y = encoder.transform(x)
    print ('label')
    print (y)

    # one hot encoding - 독립된 1,0 으로 encoding
    print ('to_categorical()')
    Y = to_categorical(y)
    print (Y)

    # label decoder : 숫자를 텍스트로 인코딩
    print ('decoding():')
    print (encoder.inverse_transform([3,2,1,0]))

def soft_max():
    df = pd.read_csv('iris.csv')
    print (df)

    X = df.values[0:, 1:5].astype(float)
    Y = df.values[0:, 5]
    #print (X)
    #print (Y)

    # one-shot encoding
    encoder = LabelEncoder()
    encoder.fit(Y)
    Y_encoded = to_categorical(encoder.transform(Y))
    # print (Y_encoded)

    # model: linear regression input dense with dim = 3
    nn = True
    model = Sequential()
    if nn:
        model.add(Dense(16, input_dim = 4, activation='relu'))
        model.add(Dense(3, activation='softmax'))
    else:
        model.add(Dense(3, input_dim = 4, activation='softmax'))
  
    # model compile: 
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # model fit
    history = model.fit(X, Y_encoded, epochs=200, batch_size=1, shuffle=False)

    # prediction
    predict = model.predict([[4.7, 3.2, 1.3, .2], [6.1, 2.9, 4.7, 1.4], [7.2,3.6,6.1,2.5]])
    print ('Predict:\n',  predict)
    
    # evalue
    loss_and_metric = model.evaluate(X, Y_encoded, batch_size=1)
    print ('Evaluate:\n', loss_and_metric)

    # 학습 정확성 값과 검증 정확성 값을 플롯팅 합니다. 
    # #print(history.history)
    plt.plot(history.history['loss'])
    plt.plot(history.history['accuracy'])
    plt.ylabel('Loss (categorical_crossentropy) & Accuracy')
    plt.legend(['loss', 'accuracy'])
    plt.xlabel('Epochs')
    plt.savefig('04_softmax_loss.png')
    #plt.show()

    # print model summary
    print ('Model summary:\n')
    model.summary()
    

if __name__ == '__main__':
    # test_onehot_encode()
    soft_max()
