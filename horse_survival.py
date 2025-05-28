from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import numpy as np

app = Flask(__name__)

# Load dataset
file_path = "data/horse_survival(in).csv"
df = pd.read_csv(file_path)

# Fill missing numeric and categorical values
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.median()))
for col in categorical_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

# Label encode all categorical cols, including 'outcome'
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Prepare features and target
X = df.drop('outcome', axis=1)
y = df['outcome']

# Train Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X, y)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form.to_dict()
    input_df = pd.DataFrame([form_data])

    # Convert numeric columns to float and categorical columns to encoded integers
    for col in input_df.columns:
        if col in label_encoders and col != 'outcome':
            # Handle unseen labels by mapping to mode category
            le = label_encoders[col]
            val = input_df.at[0, col]
            if val not in le.classes_:
                # Map unseen input to mode (most common class)
                val = le.classes_[0]
            input_df.at[0, col] = val
            input_df[col] = le.transform(input_df[col])
        else:
            # Convert numeric columns to float
            try:
                input_df[col] = input_df[col].astype(float)
            except ValueError:
                input_df[col] = 0.0  # fallback default if conversion fails

    # Reorder columns to match training
    input_df = input_df[X.columns]

    # Predict using the trained model
    prediction_encoded = rf_model.predict(input_df)[0]

    # Decode prediction back to original label
    outcome_le = label_encoders['outcome']
    outcome = outcome_le.inverse_transform([prediction_encoded])[0]

    return jsonify({'prediction': outcome})

if __name__ == '__main__':
    app.run(debug=True)
