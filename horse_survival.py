import pandas as pd

# Load the uploaded CSV file
file_path = "data/horse_survival(in).csv"
df = pd.read_csv(file_path)

# Display basic information about the dataset
df_info = df.info()
df_head = df.head()
df_description = df.describe(include='all')

df_info, df_head, df_description


# Separate numeric and categorical columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Impute numeric columns with median
df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.median()))

# Impute categorical columns with mode
for col in categorical_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])

# Verify that there are no missing values left
missing_values = df.isnull().sum()

missing_values[missing_values > 0]
# Analyze the survival outcome distribution
outcome_counts = df['outcome'].value_counts()

# Cross-tabulate outcome with selected features
age_outcome = pd.crosstab(df['age'], df['outcome'])
surgery_outcome = pd.crosstab(df['surgery'], df['outcome'])
pain_outcome = pd.crosstab(df['pain'], df['outcome'])
temp_outcome = df.groupby('outcome')['rectal_temp'].describe()
pulse_outcome = df.groupby('outcome')['pulse'].describe()

outcome_counts, age_outcome, surgery_outcome, pain_outcome, temp_outcome, pulse_outcome

import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Outcome distribution
sns.countplot(data=df, x='outcome', ax=axes[0, 0])
axes[0, 0].set_title('Survival Outcome Distribution')

# Outcome by age
sns.countplot(data=df, x='outcome', hue='age', ax=axes[0, 1])
axes[0, 1].set_title('Outcome by Age')

# Outcome by surgery
sns.countplot(data=df, x='outcome', hue='surgery', ax=axes[1, 0])
axes[1, 0].set_title('Outcome by Surgery')

# Outcome by pain level
sns.countplot(data=df, x='outcome', hue='pain', ax=axes[1, 1])
axes[1, 1].set_title('Outcome by Pain Level')
axes[1, 1].legend(loc='upper right', bbox_to_anchor=(1.3, 1))

plt.tight_layout()
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Make a copy to work on
df_model = df.copy()

# Encode categorical variables
label_encoders = {}
for col in df_model.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    df_model[col] = le.fit_transform(df_model[col])
    label_encoders[col] = le

# Split data into features and target
X = df_model.drop('outcome', axis=1)
y = df_model['outcome']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Predict and evaluate
y_pred = rf_model.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, output_dict=True)

conf_matrix, class_report
