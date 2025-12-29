# 🩺 PCOS Risk Prediction System

A machine learning–based system to predict **PCOS risk score (%)** using clinical symptoms and lab report parameters.  
This project focuses on **early risk assessment**, not medical diagnosis.

---

## 🚀 Project Overview

- Accepts lab report values and clinical symptoms as input  
- Predicts a **PCOS risk score (0–100%)**  
- Categorizes risk into **Low, Moderate, or High**  
- Uses a **calibrated Random Forest model** for meaningful probability output  

---

## 🧬 Input Parameters

The model uses the following medically relevant features:

- Age  
- Weight, Height, BMI  
- Menstrual cycle regularity  
- Cycle length  
- Hair growth (Hirsutism)  
- Skin darkening  
- Acne  
- FSH  
- LH  
- FSH/LH ratio  
- TSH  
- AMH  
- Prolactin  
- Vitamin D3  

All inputs are numeric and standardized before prediction.

---

## 🧠 Model Details

- **Algorithm:** Random Forest Classifier  
- **Probability Calibration:** Isotonic Regression  
- **Reason for Calibration:**  
  Machine learning probabilities are often uncalibrated.  
  Calibration makes risk scores more medically interpretable.
- **Class Imbalance Handling:** `class_weight="balanced"`  
- **Evaluation Metric:** ROC–AUC  


## 📊 Output Interpretation

- **PCOS Risk Score:** 0–100%  
- **Risk Categories:**
  - **Low Risk:** < 25%  
  - **Moderate Risk:** 25% – 55%  
  - **High Risk:** > 55%  
---

## ⚙️ How to Run the Project
1️⃣ Create Virtual Environment:
python -m venv myenv
myenv\Scripts\activate
2️⃣ Install Dependencies:
pip install pandas scikit-learn joblib
3️⃣ Train the Model:
python model/train_model_RF.py
4️⃣ Predict PCOS Risk:
python model/predict_risk.py

