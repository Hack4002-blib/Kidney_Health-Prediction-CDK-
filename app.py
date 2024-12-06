from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('kidney_rf_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['age']),
            float(request.form['bp']),
            float(request.form['su']),
            float(request.form['sg']),
            float(request.form['bgr']),
            float(request.form['sc']),
            float(request.form['hemo']),
            float(request.form['bu']),
            int(request.form['rbc']),
            int(request.form['pcc']),
            int(request.form['htn']),
            int(request.form['appet']), 
            int(request.form['ane'])
        ]
        scaled_features = scaler.transform([features])
        prediction = model.predict(scaled_features)
        result = "Healthy (No CKD)" if prediction[0] == 1 else "At High Risk (CKD)"
        return render_template('result.html', result=result)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
