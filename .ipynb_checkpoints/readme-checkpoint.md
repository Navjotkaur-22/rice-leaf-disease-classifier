
---

## 📌 Project Objective

Detect diseases from rice leaf images and classify them into:
- **Leaf smut**
- **Brown spot**
- **Bacterial leaf blight**

This helps farmers and agricultural systems detect plant diseases early using AI.

---

## 📊 Exploratory Data Analysis (EDA)

The notebook performs:
- Class distribution visualization  
- Image size statistics  
- Sample image previews (3 images)  
- Professional 20-image visualization grid  
- Augmentation visualization  

---

## 🧠 Models Implemented

### **1️⃣ Baseline CNN**
A small 3-layer CNN built from scratch.

### **2️⃣ CNN + Data Augmentation**
Improves generalization using:
- Rotations  
- Zoom  
- Horizontal Flip  
- Height/Width Shift  
- Brightness adjustments  

### **3️⃣ Transfer Learning (MobileNetV2)**
Used with ImageNet weights when available, otherwise fallback to no-pretrained mode.

---

## 📈 Model Evaluation

- Train / Validation Accuracy  
- Train / Validation Loss  
- Classification report (Precision, Recall, F1)  
- Confusion Matrix  
- Overall Model Comparison  
- Best model chosen for production  

---

## 🚀 How to Run Locally

1. Clone the repository / download project folder.
2. Create a virtual environment:
