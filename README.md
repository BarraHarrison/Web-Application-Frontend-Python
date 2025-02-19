# 🖼️ Web Application in Pure Python

This project demonstrates how to build a simple **image classification web application** using **pure Python** with the **Streamlit** library. Users can upload an image, and the trained **CIFAR-10 model** will predict which category it belongs to, displaying the probabilities in a bar chart. The UI is built entirely using **Streamlit**, and the results are visualized with **Matplotlib**.

---

## 📌 How the `cifar10_model.keras` Was Created

The model used in this project is a **pre-trained Convolutional Neural Network (CNN)** based on the **CIFAR-10 dataset**, which consists of 60,000 images categorized into 10 classes:

- ✈️ Airplane
- 🚗 Automobile
- 🐦 Bird
- 🐱 Cat
- 🦌 Deer
- 🐶 Dog
- 🐸 Frog
- 🐴 Horse
- 🚢 Ship
- 🚚 Truck

The model was created and trained using **TensorFlow and Keras**, and it was saved using the following method:

```python
model.save("cifar10_model.keras")
```

The saved model is then loaded in the **Streamlit app** using:

```python
model = tf.keras.models.load_model("cifar10_model.keras")
```
This allows us to perform predictions on uploaded images.

---

## 🚀 The Function of the Streamlit Library

[**Streamlit**](https://streamlit.io/) is a **Python framework** that makes it easy to build interactive web applications. In this project, Streamlit is used to:

✅ Create a **title and description** for the app:
```python
st.title("Cifar10-Model Web Classifier")
st.write("Upload any image that you think fits into one of the classes. Let's see if the prediction is correct!")
```

✅ Enable **file upload functionality**:
```python
file = st.file_uploader("Please upload an image", type=["jpg", "png"])
```

✅ **Display the uploaded image** in the UI:
```python
st.image(image, use_container_width=True)
```

✅ **Run predictions and display results** using Matplotlib:
```python
st.pyplot(fig)
```
Streamlit makes it easy to run Python code on the backend while presenting a clean UI for the user to interact with.

---

## 📊 The Matplotlib Code Explained

The predictions from the model are visualized using **Matplotlib**. Here’s how it works:

### **1️⃣ Creating the Bar Chart**
```python
fig, ax = plt.subplots()
y_position = np.arange(len(cifar10_classes))
ax.barh(y_position, predictions[0], align="center")
```
🔹 **`ax.barh(y_position, predictions[0], align="center")`** creates a **horizontal bar chart**, where each bar represents the probability of the image belonging to a CIFAR-10 class.

### **2️⃣ Setting the Labels**
```python
ax.set_yticks(y_position)
ax.set_yticklabels(cifar10_classes)
ax.invert_yaxis()
```
🔹 **`ax.set_yticks(y_position)`** ensures that each class has a tick mark.  
🔹 **`ax.set_yticklabels(cifar10_classes)`** assigns the class names to the tick marks.
🔹 **`ax.invert_yaxis()`** inverts the Y-axis so the highest probability appears on top.

### **3️⃣ Setting the Title and Axis Labels**
```python
ax.set_xlabel("Probability")
ax.set_title("CIFAR10 Predictions")
```
🔹 **`ax.set_xlabel("Probability")`** labels the X-axis.
🔹 **`ax.set_title("CIFAR10 Predictions")`** adds a title to the chart.

Finally, the chart is displayed using:
```python
st.pyplot(fig)
```
This allows Streamlit to render the **Matplotlib figure** in the web app!

---

## 🎯 Conclusion

This project highlights how you can use **Streamlit** to create a fully functional **web application using only Python**! With just a few lines of code, I:
✅ Built an **interactive UI** 🖥️  
✅ Allowed **image uploads** 📸  
✅ Used a **trained deep learning model** to classify images 🤖  
✅ Visualized predictions with **Matplotlib** 📊  

This project is a great starting point for anyone looking to explore **web applications powered by AI**. 🚀 Feel free to improve the model, enhance the UI, or extend the functionality. Happy coding! 🎉

---

### ⚡ Author
Created by **@BarraHarrison**  
GitHub: [BarraHarrison](https://github.com/BarraHarrison)  

---

