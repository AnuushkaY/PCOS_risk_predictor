# model/train_model_RF.py


import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import roc_auc_score

# Load data
df = pd.read_csv("data/cleaned_pcos_data.csv")

# convert everything to numeric (force errors to NaN)
df = df.apply(pd.to_numeric, errors="coerce")

X = df.drop("pcos", axis=1)
y = df["pcos"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 🔑 RF does not need scaling, but keep scaler for consistency
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 🌲 Random Forest
base_model = RandomForestClassifier(
    n_estimators=300,
    max_depth=6,
    min_samples_split=10,
    class_weight="balanced",
    random_state=42
)

# ⚠️ Probability calibration (VERY IMPORTANT)
model = CalibratedClassifierCV(
    estimator=base_model,
    method="isotonic",
    cv=5
)

model.fit(X_train_scaled, y_train)

# Evaluate
auc = roc_auc_score(y_test, model.predict_proba(X_test_scaled)[:, 1])
print("ROC-AUC:", round(auc, 3))


# Save
joblib.dump(model, "model/pcos_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ Random Forest model trained & saved")
