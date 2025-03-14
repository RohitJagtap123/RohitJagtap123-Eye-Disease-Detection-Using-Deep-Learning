import os
import warnings
import logging
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings("ignore", category=DeprecationWarning)
tf.get_logger().setLevel(logging.ERROR)

# Set page title
st.set_page_config(page_title="Cataract Detection", layout="centered")

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('rnet50.h5', compile=False)

model = load_model()

# Streamlit UI
st.title("Cataract Detection using ResNet50")
st.markdown("Upload an eye fundus image to check for cataracts.")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        img = image.load_img(uploaded_file, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize

        # Prediction
        prediction = model.predict(img_array)
        result = "Cataract" if prediction > 0.5 else "Normal"

        # Display results
        st.image(img, caption="Uploaded Image", use_container_width=True)
        st.subheader(f"Prediction: **{result}**")
        st.write(f"Confidence Score: **{prediction[0][0]:.2f}**")

    except Exception as e:
        st.error(f"An error occurred: {e}")
