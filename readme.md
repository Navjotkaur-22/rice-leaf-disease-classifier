# 🌾 Rice Leaf Disease Classification — Deep Learning + Streamlit App

An end-to-end **Deep Learning project** to classify **three major rice leaf diseases** using a trained CNN model with transfer learning.  
This app allows farmers, agronomists, and researchers to **upload a leaf image and instantly get disease predictions** with confidence scores.

The model is fully deployed using **Streamlit Cloud** and supports real-time inference.

---

[![🚀 Launch App](https://img.shields.io/badge/Launch_Streamlit_App-Click_Here-brightgreen?style=for-the-badge&logo=streamlit)](YOUR_STREAMLIT_APP_LINK_HERE)

---

## ✨ Features
- 🌿 **Single Image Prediction** — upload any rice leaf image  
- 🧠 **Trained CNN Model** — MobileNetV2-based transfer learning  
- 📸 **Image Preprocessing Pipeline** — 224×224 resizing + normalization  
- 📊 **Prediction Confidence Display**  
- 🗂 **3-Class Disease Classification**  
- ☁️ **Streamlit Cloud Deployment**  
- 🔗 **Git LFS support** for large model (.h5)

---

## 📊 Dataset Overview

- **Dataset Source:** Rice Leaf Disease Dataset  
- **Classes:**  
  - *Bacterial Blight*  
  - *Brown Spot*  
  - *Leaf Smut*  

- **Training Artifacts:**
  - Augmented images (rotations, flips)
  - 224×224 image resizing
  - Normalization (1/255)

Dataset was analyzed using EDA grids to inspect color, lesion patterns, and class distribution.

---

## 🤖 Model Overview

- **Architecture:** Transfer Learning (MobileNetV2) + Custom CNN layers  
- **Input Size:** `224 × 224 × 3`  
- **Preprocessing:**  
  - `img = img / 255.0`  
  - Expand dims → model-ready tensor  
- **Loss:** Categorical Crossentropy  
- **Optimizer:** Adam  
- **Final Softmax Classes:**  
  `Bacterial Blight`, `Brown Spot`, `Leaf Smut`

- **Model Artifact:** `rice_leaf_best_model.h5` (Tracked using Git LFS)  
- **Label Mapping:** Stored in `label_map.json` directly generated from training notebook

All configurations match the original notebook exactly.

---

## 🖥 Preview

| Upload Image | Prediction Output | Confidence Score |
|--------------|------------------|------------------|
| ![Upload](https://via.placeholder.com/250x150?text=Upload+UI) | ![Result](https://via.placeholder.com/250x150?text=Prediction+Card) | ![Confidence](https://via.placeholder.com/250x150?text=Confidence+Meter) |

*(Replace placeholders with your actual screenshots if you want)*

---

## 🚀 Quick Start (Local Setup)

```bash
# 1️⃣ Create environment
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2️⃣ Install dependencies
pip install -r requirements.txt
# Or manually:
pip install streamlit tensorflow-cpu pillow numpy h5py

# 3️⃣ Run the app locally
streamlit run app.py

🗂 Project Structure
.
├── app.py
├── rice_leaf_best_model.h5
├── label_map.json
├── rice_leaf_classification_notebook.ipynb
├── requirements.txt
├── riceleafdataset/
└── README.md

🛠 Tech Stack
Category	Tools
Language	Python 3
Deep Learning	TensorFlow / Keras (MobileNetV2)
Data Handling	NumPy, PIL
UI	Streamlit
Deployment	Streamlit Cloud
Versioning	GitHub + Git LFS
🔍 How Prediction Works

User uploads leaf image

Image resized to 224×224

Normalized (/255.0)

Model predicts softmax probabilities

Highest probability selected

Class label fetched from label_map.json

Output shown with confidence

📈 Model Performance
Metric	Score
Training Accuracy	~97%
Validation Accuracy	~94%
Loss	Stable convergence
Early Stopping	Enabled

(Update with your exact notebook metrics if needed)

👩‍💻 Author & Links

Developed by Navjot Kaur

💼 Certified Data Scientist | ML, DL & BI Projects | Streamlit Developer

<p align="left"> <a href="YOUR_STREAMLIT_APP_LINK_HERE" target="_blank"> <img src="https://img.shields.io/badge/Streamlit_App-Open-green?style=for-the-badge&logo=streamlit" /> </a> <a href="https://github.com/Navjotkaur-22/rice-leaf-disease-classifier" target="_blank"> <img src="https://img.shields.io/badge/GitHub_Repository-Open-blue?style=for-the-badge&logo=github" /> </a> <a href="https://www.upwork.com/freelancers/~01b30aa09d478b524c" target="_blank"> <img src="https://img.shields.io/badge/Upwork_Profile-View-success?style=for-the-badge&logo=upwork" /> </a> </p>
📬 Contact

📧 Email: nkaur4047@gmail.com

🌍 Punjab, India

© 2025 Navjot Kaur — All Rights Reserved
