# Cataract Detection using ResNet50

## 📌 Overview
This project is a **Cataract Detection System** built using **ResNet50** and **Streamlit**. It allows users to upload an eye fundus image and predicts whether the image indicates **Cataract** or **Normal** condition.

## 🚀 Features
- **Deep Learning Model**: Uses a pre-trained ResNet50 model.
- **User-Friendly UI**: Built with Streamlit for a simple and interactive experience.
- **Real-Time Predictions**: Upload an image and get instant results.
- **Confidence Score**: Displays the confidence level of the prediction.

## 🛠️ Technologies Used
- Python
- TensorFlow/Keras
- Streamlit
- NumPy
- Pillow (PIL)

## 📂 Project Structure
```
📁 ocular-disease-recognition-odir5k
│── 📂 ODIR-5K                   # Dataset folder (if applicable)
│── 📂 preprocessed_images       # Preprocessed image storage
│── 📄 app.py                    # Streamlit application
│── 📄 rnet50.h5                 # Trained ResNet50 model
│── 📄 full_df.csv               # CSV file with dataset details (if applicable)
│── 📄 Smart_Bridge_Project.ipynb # Jupyter notebook (optional)
│── 📄 README.md                 # Documentation
```

## 🔧 Installation
### 1️⃣ Clone the repository:
```sh
git clone https://github.com/your-username/ocular-disease-recognition.git
cd ocular-disease-recognition-odir5k
```

### 2️⃣ Create a virtual environment (Recommended):
```sh
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
```

### 3️⃣ Install dependencies:
```sh
pip install -r requirements.txt
```
_(If `requirements.txt` is not available, install manually:)_
```sh
pip install streamlit tensorflow numpy pillow
```

## ▶️ Run the Application
```sh
streamlit run app.py
```

## 📷 Usage
1. Click on the **"Upload an image"** button and select an eye fundus image.
2. The model will analyze the image and display the result (**Cataract** or **Normal**).
3. The **confidence score** is also displayed.

## ⚠️ Troubleshooting
### 🔹 TensorFlow Installation Issues
- Ensure you have the correct Python version installed (**Python 3.8+ recommended**).
- If TensorFlow is not installing, try:
  ```sh
  pip install tensorflow --no-cache-dir
  ```

### 🔹 Streamlit Not Found
- Run:
  ```sh
  pip install streamlit
  ```

### 🔹 Virtual Environment Issues
- Make sure you have activated the virtual environment before running the script.
  ```sh
  source .venv/bin/activate  # Linux/Mac
  .venv\Scripts\activate     # Windows
  ```

## 🏆 Acknowledgments
- **ResNet50**: A powerful deep learning model for image classification.
- **Streamlit**: For creating a simple UI.
- **TensorFlow/Keras**: For deep learning implementation.

## 📜 License
This project is open-source and available under the **MIT License**.

---
🔗 **Developed by [Your Name]**

