# Importing required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score
import joblib

# Load the dataset
data = pd.read_csv('kidney_disease.csv')

# Handle missing values in numerical columns
numerical_columns = ['age', 'bp', 'su', 'sg', 'bgr', 'sc', 'hemo', 'bu']
data[numerical_columns] = data[numerical_columns].apply(lambda x: x.fillna(x.mean()))


# Handle missing values in categorical columns
categorical_columns = ['rbc', 'pcc', 'htn', 'appet', 'ane', 'classification']
data[categorical_columns] = data[categorical_columns].apply(lambda x: x.fillna(x.mode()[0]))

# Convert categorical values to binary encoding
binary_mapping = {
    'rbc': {'normal': 0, 'abnormal': 1},
    'pcc': {'notpresent': 0, 'present': 1},
    'htn': {'no': 0, 'yes': 1},
    'appet': {'poor': 0, 'good': 1},
    'ane': {'no': 0, 'yes': 1}
}
for col, mapping in binary_mapping.items():
    data[col] = data[col].map(mapping)

# Encode target column and drop rows with NaN in the target
data['classification'] = data['classification'].map({'notckd': 1, 'ckd': 0})
data = data.dropna(subset=['classification'])

# Feature selection
selected_features = ['age', 'bp', 'su', 'sg', 'bgr', 'sc', 'hemo', 'bu', 'rbc', 'pcc', 'htn', 'appet', 'ane']
X = data[selected_features]
y = data['classification']

# Scale the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train the model using Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("ROC-AUC Score:", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))

# Save the model and scaler
joblib.dump(model, 'kidney_rf_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Model and scaler saved successfully.")
