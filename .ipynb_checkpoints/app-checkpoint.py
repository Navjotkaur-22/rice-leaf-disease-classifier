import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import json

# ------------------------------
# STREAMLIT PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="Rice Leaf Disease Classifier", layout="centered")
st.title("🌾 Rice Leaf Disease Classification")
st.write("Upload a rice leaf image to classify the disease using the trained CNN model.")

# ------------------------------
# LOAD MODEL
# ------------------------------
@st.cache_resource
def load_cnn_model():
    model = load_model("rice_leaf_best_model.h5")
    return model

model = load_cnn_model()

# ------------------------------
# LOAD CLASS LABELS (from notebook)
# ------------------------------
# Should match notebook's "label_map.json"
with open("label_map.json", "r") as f:
    labels_map = json.load(f)

# label_map.json was saved as: {0:"Bacterial Blight", 1:"Brown Spot", 2:"Leaf Smut"}
class_names = [labels_map[str(i)] for i in range(len(labels_map))]

# ------------------------------
# PREPROCESS FUNCTION (exact notebook version)
# ------------------------------
IMG_SIZE = (224, 224)   # from notebook
def preprocess_image(img):
    img = img.resize(IMG_SIZE)
    img = img_to_array(img)
    img = img / 255.0        # EXACT notebook normalization
    img = np.expand_dims(img, axis=0)
    return img

# ------------------------------
# PREDICTION FUNCTION
# ------------------------------
def predict(img):
    processed = preprocess_image(img)
    preds = model.predict(processed)
    class_id = np.argmax(preds)
    confidence = float(np.max(preds))
    predicted_label = class_names[class_id]
    return predicted_label, confidence

# ------------------------------
# STREAMLIT UI
# ------------------------------
uploaded = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    if st.button("🔍 Predict"):
        with st.spinner("Analyzing…"):
            label, conf = predict(img)

        st.success(f"🌱 Prediction: **{label}**")
        st.write(f"📊 Confidence: **{conf*100:.2f}%**")

        # EXTRA INFO
        if label.lower() == "bacterial blight":
            st.info("👉 Bacterial Blight causes yellowing and streaks.")
        elif label.lower() == "brown spot":
            st.info("👉 Brown Spot shows brown circular lesions.")
        elif label.lower() == "leaf smut":
            st.info("👉 Leaf Smut forms blackish smut-like spots.")
