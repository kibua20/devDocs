#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

from tensorflow import keras

# --------------------------------------------------------------------------------------------------------
# Save keras model: code sample from https://www.tensorflow.org/guide/keras/save_and_serialize?hl=ko
def save_model():
    # Create a simple model.
    inputs = keras.Input(shape=(32,))
    outputs = keras.layers.Dense(1)(inputs)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mean_squared_error")
    
    # Train the model.
    test_input = np.random.random((128, 32))
    test_target = np.random.random((128, 1))

    model.fit(test_input, test_target)

    # Calling `save('my_model')` creates a SavedModel folder `my_model`.
    model.save("my_model.h5")

# --------------------------------------------------------------------------------------------------------
# run the app.
def load_model():
    # It can be used to reconstruct the model identically.
    reconstructed_model = keras.models.load_model("my_model.h5")

    # Train the model.
    test_input = np.random.random((128, 32))
    test_target = np.random.random((128, 1))

    # The reconstructed model is already compiled and has retained the optimizerstate, so training can resume:
    reconstructed_model.fit(test_input, test_target)

    print ('Reconstruced Model:')
    reconstructed_model.summary()

# --------------------------------------------------------------------------------------------------------
# run the app.
if __name__ == "__main__":
    save_model()
    load_model()