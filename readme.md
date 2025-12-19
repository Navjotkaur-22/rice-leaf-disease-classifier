# 🌾 Rice Leaf Disease Classification — Deep Learning + Streamlit App

An end-to-end **Deep Learning project** to classify **three major rice leaf diseases** using a trained CNN model with transfer learning.  
This app allows farmers, agronomists, and researchers to **upload a leaf image and instantly get disease predictions** with confidence scores.

The model is fully deployed using **Streamlit Cloud** and supports real-time inference.

---

[![🚀 Launch App](https://img.shields.io/badge/Launch_Streamlit_App-Click_Here-brightgreen?style=for-the-badge&logo=streamlit)](https://rice-leaf-disease-classifier-fiiamasjb8gsanuahw48rc.streamlit.app/)

---

## ✨ Features
- 🌿 **Single Image Prediction**  
- 🧠 **MobileNetV2 Transfer Learning Model**  
- 📸 **224×224 Preprocessing + Normalization**  
- 📊 **Confidence Score Display**  
- 🗂 **3-Class Rice Disease Classification**  
- ☁️ **Live on Streamlit Cloud**  
- 🔗 **Git LFS for model.h5**

---

## 📊 Dataset Overview
- **Classes:**  
  - Bacterial Blight  
  - Brown Spot  
  - Leaf Smut  

- **Training Preprocessing:**  
  - Image Augmentation  
  - 224×224 resizing  
  - Normalization (/255.0)

---

## 🤖 Model Overview
- **Architecture:** MobileNetV2 + Custom Dense Layers  
- **Input Size:** 224×224×3  
- **Loss:** Categorical Crossentropy  
- **Optimizer:** Adam  
- **Artifact:** `rice_leaf_best_model.h5` (LFS)  
- **Labels:** `label_map.json`

---

## 🚀 Quick Start (Local Setup)

~~~bash
# 1️⃣ Create environment
python -m venv .venv
. .venv/bin/activate    # Windows: .venv\Scripts\activate

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run
streamlit run app.py
~~~

---

## 🗂 Project Structure

~~~text
.
├── app.py
├── rice_leaf_best_model.h5
├── label_map.json
├── rice_leaf_classification_notebook.ipynb
├── requirements.txt
├── riceleafdataset/
└── README.md
~~~

---

## 🛠 Tech Stack

| Category | Tools |
|----------|--------|
| Language | Python 3 |
| Deep Learning | TensorFlow / Keras |
| UI | Streamlit |
| Handling | NumPy, PIL |
| Deployment | Streamlit Cloud |
| Storage | Git LFS |

---

## 🔍 How Prediction Works
1. User uploads image  
2. Resize → 224×224  
3. Normalize → /255  
4. Predict via MobileNetV2  
5. Softmax scores generated  
6. Highest probability picked  
7. Display disease + confidence  

---

## 📈 Model Performance  
| Metric | Score |
|--------|--------|
| Training Accuracy | ~97% |
| Validation Accuracy | ~94% |
| Loss | Stable |
| Early Stopping | Enabled |

---

## ✨ Author  

👩🏻‍💻 **Navjot Kaur**  
MSc (IT) | Certified Data Scientist | Streamlit Developer  
📍 Jalandhar, Punjab  
📧 **Email:** nkaur4047@gmail.com  

<p align="center">
<a href="https://github.com/Navjotkaur-22" target="_blank"><img src="https://img.shields.io/badge/GitHub-Navjotkaur--22-black?logo=github&style=for-the-badge"/></a>
<a href="https://www.linkedin.com/in/navjot-kaur-b61aab299/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-Navjot_Kaur-blue?logo=linkedin&style=for-the-badge"/></a>
<a href="https://www.upwork.com/freelancers/~01b30aa09d478b524c" target="_blank"><img src="https://img.shields.io/badge/Upwork-Hire_Me-brightgreen?logo=upwork&style=for-the-badge"/></a>
</p>

---

**© 2025 Navjot Kaur — All Rights Reserved**
