import pandas as pd
import joblib

# Load model & scaler
model = joblib.load("model/pcos_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# 🔑 Correct mapping (MATCHES TRAINING)
COLUMN_MAPPING = {
    'Age (yrs)': 'age',
    'Weight (Kg)': 'weight',
    'Height(Cm)': 'height',
    'BMI': 'bmi',
    'Cycle(R/I)': 'irregular_cycle',   # ✅ FIX
    'Cycle length(days)': 'cycle_length',
    'hair growth(Y/N)': 'hair_growth',
    'Skin darkening (Y/N)': 'skin_darkening',
    'Acne(Y/N)': 'acne',
    'FSH(mIU/mL)': 'fsh',
    'LH(mIU/mL)': 'lh',
    'FSH/LH': 'lh_fsh_ratio',           # ✅ FIX
    'TSH (mIU/L)': 'tsh',
    'AMH(ng/mL)': 'amh',
    'PRL(ng/mL)': 'prolactin',          # ✅ FIX
    'Vit D3 (ng/mL)': 'vitamin_d'       # ✅ FIX
}

def predict_pcos_risk(lab_input):
    df = pd.DataFrame([lab_input])

    # Rename lab columns → model columns
    df.rename(columns=COLUMN_MAPPING, inplace=True)

    # Ensure correct order
    df = df[scaler.feature_names_in_]

    # Scale
    df_scaled = scaler.transform(df)

    # 🔑 TRUE probability
    prob = model.predict_proba(df_scaled)[0][1]
    risk_percent = round(prob * 100, 2)

    # ---------------------------
    # Risk bands (medical)
    # ---------------------------
    if risk_percent < 20:
        level = "Low Risk"
    elif risk_percent < 40:
        level = "Borderline Risk"
    elif risk_percent < 60:
        level = "Moderate Risk"
    else:
        level = "High Risk"

    return risk_percent, level


# 🔍 Test
if __name__ == "__main__":
    # sample_input = {
    #     'Age (yrs)': 23,
    #     'Weight (Kg)': 58,
    #     'Height(Cm)': 160,
    #     'BMI': 22.6,
    #     'Cycle(R/I)': 1,              # 1 = irregular
    #     'Cycle length(days)': 36,
    #     'hair growth(Y/N)': 1,
    #     'Skin darkening (Y/N)': 0,
    #     'Acne(Y/N)': 1,
    #     'FSH(mIU/mL)': 5.2,
    #     'LH(mIU/mL)': 11.1,
    #     'FSH/LH': 0.47,
    #     'TSH (mIU/L)': 2.4,
    #     'AMH(ng/mL)': 6.3,
    #     'PRL(ng/mL)': 18,
    #     'Vit D3 (ng/mL)': 16
    # }
    
    sample_input = {
        'Age (yrs)': 26,
        'Weight (Kg)': 85,
        'Height(Cm)': 155,
        'BMI': 35.4,
        'Cycle(R/I)': 1,
        'Cycle length(days)': 60,
        'hair growth(Y/N)': 1,
        'Skin darkening (Y/N)': 1,
        'Acne(Y/N)': 1,
        'FSH(mIU/mL)': 3.1,
        'LH(mIU/mL)': 18.9,
        'FSH/LH': 0.16,
        'TSH (mIU/L)': 5.6,
        'AMH(ng/mL)': 11.8,
        'PRL(ng/mL)': 31,
        'Vit D3 (ng/mL)': 8
    }




    score, level = predict_pcos_risk(sample_input)
    print("PCOS Risk Score:", score, "%")
    print("Risk Level:", level)
