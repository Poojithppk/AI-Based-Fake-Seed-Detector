import streamlit as st
import tensorflow as tf
import cv2
import numpy as np
from PIL import Image
from tensorflow.keras.applications.efficientnet import preprocess_input

st.set_page_config(page_title="Fake Seed Detector", layout="centered")
st.title("🌱 Fake Seed Detector")

model = tf.keras.models.load_model("seed_model.h5")

IMG_SIZE = 224
THRESHOLD = 0.8

uploaded_file = st.file_uploader("Upload seed image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", width = 250)

    img = np.array(image)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    prob_fake = model.predict(img)[0][0]

    if prob_fake >= THRESHOLD:
        st.error(f" FAKE SEED\nConfidence: {prob_fake:.2f}")
    else:
        st.success(f"GENUINE SEED\nConfidence: {1 - prob_fake:.2f}")