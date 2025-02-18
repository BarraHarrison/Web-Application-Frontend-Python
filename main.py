# Web Application in Pure Python
# Using the Package Streamlit to build a UI
import numpy as np 
import matplotlib.pyplot as plt 
import streamlit as st 

from PIL import Image

import tensorflow as tf 
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train / 255
x_test = x_test / 255

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

model = Sequential([
    Flatten(input_shape=(32, 32, 3)),
    Dense(1000, activation="relu"),
    Dense(10, activation="softmax")
])

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(x_train, y_train, batch_size=64, epochs=10, validation_data=(x_val, y_val))
model.save("cifar10_model.keras")