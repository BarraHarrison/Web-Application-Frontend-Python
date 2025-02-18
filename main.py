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
        st.image(image, use_container_width=True)

        resized_image = image.resize((32, 32))
        image_array = np.array(resized_image / 255.0)
        image_array = image_array.reshape((1, 32, 32, 3))

        model = tf.keras.models.load_model("cifar10_model.keras")

        predictions = model.predict(image_array)
        cifar10_classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

        fig, ax = plt.subplots()
        y_position = np.arange(len(cifar10_classes))
        ax.barh(y_position, predictions[0], align="center")
        ax.set_yticks(y_position)
        ax.set_yticklabels(cifar10_classes)
        ax.invert_yaxis()
        ax.set_xlabel("Probability")
        ax.set_title("CIFAR10 Predictions")

        st.pyplot(fig)

    else:
        st.text("You have not uploaded an image yet.")

if __name__ == "__main__":
    main()