import pandas as pd

# Load dataset
df = pd.read_excel("data/PCOS_data_without_infertility.xlsx")
# print(df.columns.tolist())

# Select only required columns
selected_columns = [
    ' Age (yrs)',
    'Weight (Kg)',
    'Height(Cm) ',
    'BMI',
    'Cycle(R/I)',
    'Cycle length(days)',
    'hair growth(Y/N)',
    'Skin darkening (Y/N)',
    'Pimples(Y/N)',
    'FSH(mIU/mL)',
    'LH(mIU/mL)',
    'FSH/LH',
    'TSH (mIU/L)',
    'AMH(ng/mL)',
    'PRL(ng/mL)',
    'Vit D3 (ng/mL)',
    'PCOS (Y/N)'
]

df = df[selected_columns]

# Rename columns (clean names)
df.columns = [
    'age',
    'weight',
    'height',
    'bmi',
    'irregular_cycle',
    'cycle_length',
    'hair_growth',
    'skin_darkening',
    'acne',
    'fsh',
    'lh',
    'lh_fsh_ratio',
    'tsh',
    'amh',
    'prolactin',
    'vitamin_d',
    'pcos'
]

# Handle missing values
df.fillna(df.median(numeric_only=True), inplace=True)

# Save cleaned data
df.to_csv("data/cleaned_pcos_data.csv", index=False)

print("✅ Cleaned PCOS dataset saved successfully")
