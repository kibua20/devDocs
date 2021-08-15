#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist

from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Input, Reshape, Flatten
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import UpSampling2D, Conv2D, MaxPool2D
from tensorflow.keras.layers import Activation, LeakyReLU

import matplotlib.pyplot as plt

# 랜덤 시드 설정
np.random.seed(0)
tf.random.set_seed(0)

# 데이터 불러오기
(X_raw, _), (_, _) = mnist.load_data()

# 변수 설정
n_img = X_raw.shape[0]
epoch = 3000
n_batch = 100

# 데이터 전처리
X_re = X_raw.reshape(n_img, 28, 28, 1)
scale_c = 255/2
X = (X_re - scale_c) / scale_c
real_1 = np.ones((n_batch, 1))
fake_0 = np.zeros((n_batch, 1))

# 생성자
input_layer1 = Input(shape=(100,))
x1 = Dense(64*7*7)(input_layer1)
x1 = BatchNormalization()(x1)
x1 = Activation(LeakyReLU(0.3))(x1)
x1 = Reshape((7,7,64))(x1)
x1 = UpSampling2D()(x1)
x1 = Conv2D(32, kernel_size=(3,3), padding='same')(x1)
x1 = BatchNormalization()(x1)
x1 = Activation(LeakyReLU(0.3))(x1)
x1 = UpSampling2D()(x1)
output_layer1 = Conv2D(1, kernel_size=(3,3), padding='same', activation='tanh')(x1)
generator = Model(input_layer1, output_layer1)
generator.summary()

# 판별자
input_layer2 = Input(shape=(28, 28, 1))
x2 = Conv2D(64, kernel_size=(5,5), padding='same')(input_layer2)
x2 = Activation(LeakyReLU(0.3))(x2)
x2 = Dropout(0.25)(x2)
x2 = Conv2D(128, kernel_size=(3,3), padding='same')(x2)
x2 = Activation(LeakyReLU(0.3))(x2)
x2 = Dropout(0.25)(x2)
x2 = Flatten()(x2)
output_layer2 = Dense(1, activation='sigmoid')(x2)
discriminator = Model(input_layer2, output_layer2)
discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
discriminator.trainable = False
discriminator.summary()

# GAN
input_gan = Input(shape=(100,))
output_dis = discriminator(generator(input_gan))
gan = Model(input_gan, output_dis)
gan.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
gan.summary()

# 학습
loss_disc_real = [0]*epoch
loss_disc_fake = [0]*epoch
loss_disc_avg = [0]*epoch
loss_gan = [0]*epoch
acc_disc_real = [0]*epoch
acc_disc_fake = [0]*epoch
acc_disc_avg = [0]*epoch
acc_gan = [0]*epoch

for i in range(0, epoch):
    # 실제 데이터 판별
    idx = np.random.randint(0, n_img, n_batch)
    imgs = X[idx]
    res_real = discriminator.train_on_batch(imgs, real_1)
    
    # 가짜 데이터 생성 및 판별
    fake = np.random.normal(0, 1, size=(n_batch, 100))
    gen_imgs = generator.predict(fake)
    res_fake = discriminator.train_on_batch(gen_imgs, fake_0)
    
    # 판별 손실 평균 & 정확도 평균
    loss_disc_avg_ith = np.add(res_real[0],res_fake[0])*0.5
    acc_disc_avg_ith = np.add(res_real[1],res_fake[1])*0.5
    
    # GAN 결과
    res_gan = gan.train_on_batch(fake, real_1)

    # 정확도 및 손실
    loss_disc_real[i] = res_real[0]
    loss_disc_fake[i] = res_fake[0]
    loss_disc_avg[i] = loss_disc_avg_ith
    loss_gan[i] = res_gan[0]
    
    acc_disc_real[i] = res_real[1]
    acc_disc_fake[i] = res_fake[1]
    acc_disc_avg[i] = acc_disc_avg_ith
    acc_gan[i] = res_gan[1]
    
    print('epoch:%d'%i,
          ' 판별손실평균:%.4f'%loss_disc_avg_ith,
          ' 판별정확도평균:%.4f'%acc_disc_avg_ith,
          ' 생성손실:%.4f'%res_gan[0], 
          ' 생성정확도:%.4f'%res_gan[1])

# 손실 그래프
epo = np.arange(0, epoch)

plt.figure()
plt.plot(epo, loss_disc_real,'y:',label='disc_real')
plt.plot(epo, loss_disc_fake,'g-.',label='disc_fake')
plt.plot(epo, loss_disc_avg,'b--',label='disc_avg')
plt.plot(epo, loss_gan,'r',label='generator')
plt.title('LOSS')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend()
#plt.show()
plt.savefig('10_gan_loss.png')

# 정확도 그래프
plt.figure()
plt.plot(epo, acc_disc_real,'y:',label='disc_real')
plt.plot(epo, acc_disc_fake,'g-.',label='disc_fake')
plt.plot(epo, acc_disc_avg,'b--',label='disc_avg')
plt.plot(epo, acc_gan,'r',label='generator')
plt.title('ACCURACY')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()
#plt.show()
plt.savefig('10_gan_accuracy.png')

# epoch=3000
gen_imgs = 0.5 * gen_imgs + 0.5
plt.figure(figsize=(10, 5))
for i in range(3*5):
    plt.subplot(3, 5, i+1)
    plt.imshow(gen_imgs[i].reshape((28, 28)), cmap='Greys')
#plt.show()
plt.savefig('10_gan_genimgs.png')
