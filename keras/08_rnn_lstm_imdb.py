#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import MaxPooling1D

import matplotlib.pyplot as plt
import re

def sentiment_predict(new_sentence):
  # 알파벳과 숫자를 제외하고 모두 제거 및 알파벳 소문자화
  new_sentence = re.sub('[^0-9a-zA-Z ]', '', new_sentence).lower()

  # 정수 인코딩
  encoded = []
  for word in new_sentence.split():
    # 단어 집합의 크기를 10,000으로 제한.
    try :
      if word_to_index[word] <= 10000:
        encoded.append(word_to_index[word]+3)
      else:
    # 10,000 이상의 숫자는 <unk> 토큰으로 취급.
        encoded.append(2)
    # 단어 집합에 없는 단어는 <unk> 토큰으로 취급.
    except KeyError:
      encoded.append(2)

  pad_new = sequence.pad_sequences([encoded], maxlen = 100) # 패딩
  score = float(model.predict(pad_new)) # 예측
  if(score > 0.5):
    print("{:.2f}% 확률로 긍정 리뷰입니다.".format(score * 100))
  else:
    print("{:.2f}% 확률로 부정 리뷰입니다.".format((1 - score) * 100))



# 데이터 불러오기 - imdb 데이터는 리뷰에 대한 텍스트와 해당 리뷰가 긍정인 경우 1을 부정인 경우 0으로 표시한 레이블로 구성된 데이터
# https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data
# https://wikidocs.net/24586
(X_tn0,y_tn0),(X_te0,y_test)=imdb.load_data(num_words=2000)


# 원본 데이터 차원 확인
print('X train shape:', X_tn0.shape)
print('Y train shape:', y_tn0.shape)
print('X test shape:', X_te0.shape)
print('Y test shape:', y_test.shape)

# 트레이닝/밸리데이션셋 분리
X_train = X_tn0[0:20000]
y_train = y_tn0[0:20000]
X_valid = X_tn0[20000:25000]
y_valid = y_tn0[20000:25000]

# 피쳐 데이터 형태 확인:  imdb 데이터는 토큰화와 정수 인코딩이라는 텍스트 전처리가 끝난 상태 . 
# IMDB 리뷰 데이터는 전체 데이터에서 각 단어들의 등장 빈도에 따라서 인덱스를 부여했습니다. 숫자가 낮을수록 이 데이터에서 등장 빈도 순위가 높음
# y 가 1이면 긍정, y가 0이면 부정임
print ('X_train[0]:', X_train[0])
print ('y_train[0]:', y_train[0])

# imdb 실제 리뷰 내용 text로 확인하기
word_to_index = imdb.get_word_index()
index_to_word={}
for key, value in word_to_index.items():
    index_to_word[value+3] = key

print('빈도수 상위 1등 단어 : {}'.format(index_to_word[4]))
for index, token in enumerate(("<pad>", "<sos>", "<unk>")):
  index_to_word[index]=token
print(' '.join([index_to_word[index] for index in X_train[0]]))
# end 

# 개별 피쳐 크기 확인
print ('# of features (X train) :', len(X_train[0]), len(X_train[1]))

# 타겟 클래스 확인
print ('y test:', set(y_test))
print ('y test len:', len(set(y_test)))

# 피쳐 데이터 변형 - 단어 중에서 가장 많이 쓰이는 단어는 남기고 나머지 단어는 0 으로 저장
X_train = sequence.pad_sequences(X_train, maxlen=100)
X_valid = sequence.pad_sequences(X_valid, maxlen=100)
X_test = sequence.pad_sequences(X_te0, maxlen=100)

# LSTM 모형 생성; Embedding - Conv1D, MaxPooling1D, LSTM, Dropout, Dense
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=100))
model.add(Conv1D(50, kernel_size=3, padding='valid', activation='relu'))
model.add(MaxPooling1D(pool_size=3))
model.add(LSTM(100, activation='tanh'))
model.add(Dropout(0.25))
model.add(Dense(1, activation='sigmoid'))
model.summary()

# 모형 컴파일과 학습
model.compile(loss='binary_crossentropy', optimizer='adam',   metrics=['accuracy'])
epochs = 10
hist = model.fit(X_train, y_train,  batch_size=100, epochs=epochs, validation_data=(X_valid, y_valid))

# Model training Evaluate
print ('\nModel training evaluate:')
print(model.evaluate(X_train, y_train)[1])
print(model.evaluate(X_valid, y_valid)[1])

# 테스트 데이터 평가
score, acc = model.evaluate(X_test, y_test, batch_size=100, verbose=1)
print('Test score:', score)
print('Test accuracy:', acc)
print(model.evaluate(X_test, y_test)[1])

# Sample String test
negative_str = """This movie was just way too overrated. The fighting was not professional and in slow motion. 
I was expecting more from a 200 million budget movie. The little sister of T.Challa was just trying too hard to be funny. 
The story was really dumb as well. Don't watch this movie if you are going because others say its great unless you are a Black Panther fan or Marvels fan."""

postive_str = """I was lucky enough to be included in the group to see the advanced screening in Melbourne on the 15th of April, 2012. And, 
firstly, I need to say a big thank-you to Disney and Marvel Studios. 
Now, the film... how can I even begin to explain how I feel about this film? It is, as the title of this review says a 'comic book triumph'. 
I went into the film with very, very high expectations and I was not disappointed. 
Seeing Joss Whedon's direction and envisioning of the film come to life on the big screen is perfect. 
The script is amazingly detailed and laced with sharp wit a humor. 
The special effects are literally mind-blowing and the action scenes are both hard-hitting and beautifully choreographed."""
sentiment_predict(negative_str)
sentiment_predict(postive_str)


# 정확도 학습 그래프
epoch = np.arange(1,epochs)
acc_train = hist.history['accuracy'] 
acc_valid = hist.history['val_accuracy']
loss_train = hist.history['loss'] 
loss_valid = hist.history['val_loss']

plt.figure(figsize=(15,5))
plt.subplot(121)
plt.plot(epoch, acc_train,'b', marker='.', label='train_acc')
plt.plot(epoch, acc_valid,'r--', marker='.', label='valid_acc')
plt.title('Accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()
plt.subplot(122)
plt.plot(epoch,loss_train,'b', marker='.',  label='train_loss')
plt.plot(epoch,loss_valid,'r--', marker='.', label='valid_loss')
plt.title('Loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
#plt.show()
plt.savefig('08_rnn_imdb.png')


