# 🩺 PCOS Risk Prediction System
### *Machine Learning–Based Early Risk Assessment Tool*

A machine learning–based system to predict **PCOS Risk Score (%)** using **clinical symptoms and lab report parameters**.  

> ⚠️ This project is intended for **early risk assessment only** and **not for medical diagnosis**.

---

## 🚀 Project Overview

- 📋 Accepts **lab report values & clinical symptoms** as input  
- 📊 Predicts a **PCOS risk score (0–100%)**  
- 🚦 Categorizes risk into:
  - Low Risk  
  - Moderate Risk  
  - High Risk  
- 🌲 Uses a **calibrated Random Forest model** for medically meaningful probabilities  

---

## 🧬 Input Parameters

The model uses the following **medically relevant features**:

- 🧑 Age  
- ⚖️ Weight, Height, BMI  
- 🔄 Menstrual cycle regularity  
- 📆 Cycle length  
- 🧔 Hair growth (Hirsutism)  
- 🌑 Skin darkening  
- 😖 Acne  
- 🧪 FSH  
- 🧪 LH  
- ⚖️ FSH/LH ratio  
- 🦋 TSH  
- 🧬 AMH  
- 🧪 Prolactin  
- ☀️ Vitamin D3  

All inputs are **numeric** and **standardized** before prediction.

---

## 🧠 Model Details

- **Algorithm:** 🌲 Random Forest Classifier  
- **Probability Calibration:** 📐 Isotonic Regression  
- **Why Calibration?**  
  Raw ML probabilities are often unreliable.  
  Calibration improves **medical interpretability** of risk scores.
- **Class Imbalance Handling:**  
  `class_weight="balanced"`  
- **Evaluation Metric:**  
  ROC–AUC  

---

## 📊 Output Interpretation

- **PCOS Risk Score:** `0–100 %`

### 🚦 Risk Categories
- 🟢 **Low Risk:** `< 25%`  
- 🟡 **Moderate Risk:** `25% – 55%`  
- 🔴 **High Risk:** `> 55%`  

---

## ⚙️ How to Run the Project

### 1️⃣ Create Virtual Environment
```bash
python -m venv myenv
myenv\Scripts\activate
```

### 2️⃣ Install Dependencies:
```bash
pip install pandas scikit-learn joblib
```

### 3️⃣ Train the Model:
```bash
python model/train_model_RF.py
```

### 4️⃣ Predict PCOS Risk:
```bash
python model/predict_risk.py
```
