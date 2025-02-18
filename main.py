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