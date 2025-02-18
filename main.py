# Web Application in Pure Python
# Using the Package Streamlit to build a UI
import numpy as np 
import matplotlib.pyplot as plt 
import streamlit as st 
from PIL import Image
import tensorflow as tf 

def main():
    st.title("Cifar10-Model Web Classifier")
    st.write("Upload any image that you think fits into one of the classes. Let's see if the prediction is correct!")
    file = st.file_uploader("Please upload an image", type=["jpg", "png"])

    if file:
        image = Image.open(file)
        st.image(image, use_column_width=True)
    else:
        st.text("You have not uploaded an image yet.")