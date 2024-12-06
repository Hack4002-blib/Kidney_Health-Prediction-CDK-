# Kidney_Health-Prediction-CDK-
# Kidney Health Prediction System

## Overview
The **Kidney Health Prediction System** is a machine learning-based application designed to assist healthcare professionals in predicting Chronic Kidney Disease (CKD) risk. This software provides an efficient, user-friendly solution tailored for use by hospitals, diagnostic labs, and specialist urologists. It is built to enhance healthcare decision-making while being responsible and secure, as it is not accessible to the general public to prevent misuse.

This project is submitted as a **Second Year BSIT Project** for the **4th Talent Festival 2024 at Government College University Hyderabad (GCUH)**.

---

## Key Features
1. **Efficient Prediction**: Predicts kidney health risk based on key medical indicators such as blood pressure, hemoglobin levels, blood urea, and more.
2. **Professional Design**: Exclusively built for healthcare professionals like urologists, lab technicians, and hospital staff.
3. **User-Friendly Interface**:
   - Clean web-based GUI using Flask.
   - Simple input forms with intuitive navigation.
4. **Data Handling**:
   - Utilizes real-world datasets for training the prediction model.
   - Ensures data accuracy and scalability.
5. **Machine Learning Integration**:
   - Random Forest Classifier for predictions.
   - Preprocessing with `scaler.pkl` for data normalization.
6. **Deployment-Ready**: Includes all components required for local deployment and testing.

---

## Project Directory Structure
```plaintext
Kidney-Health-Prediction/
├── mode_training.py         # Script to train the model
├── app.py                   # Main Flask application file
├── kidney_disease.csv       # Dataset used for training
├── Introduction to Kidney Health and CKD Prediction Software.ppt # Project presentation
├── source_code.ipynb        # Jupyter Notebook for data analysis and model development
├── scaler.pkl               # Pretrained scaler for data preprocessing
├── kidney_rf_model.pkl      # Pretrained Random Forest model
├── .venv/                   # Virtual environment folder
├── static/                  # Static files directory
│   ├── styles.css           # CSS for styling
│   └── images/
│       └── bcg.webp         # Background image
├── templates/               # HTML templates directory
│   ├── index.html           # Homepage with input form
│   └── result.html          # Results page
Disclaimer
This software is not intended for general public use and is tailored for healthcare professionals only to ensure responsible usage and avoid misuse.This software, Kidney Health Prediction System, is developed as a learning project to explore the implementation of Artificial Intelligence (AI) and Machine Learning (ML) in the medical and healthcare industry. While every effort has been made to ensure the accuracy and functionality of this software, it is important to understand its limitations and intended purpose:

Limited Dataset:
This model was trained on a limited dataset, which may not comprehensively cover all possible scenarios or patient conditions. As a result, the predictions may have a degree of uncertainty and should not be solely relied upon for medical decisions.

Accuracy:
The current model achieves a prediction accuracy of approximately 70–80% based on the training data. While this is a promising start, it is not sufficient for use in critical or life-altering medical decisions. The software is intended to demonstrate how AI and ML can be applied in healthcare, rather than provide definitive diagnoses.

Not a Substitute for Professional Medical Advice:
This software is not a replacement for medical expertise. Users are strongly advised to seek proper consultation from a qualified healthcare professional, specialist urologist, or hospital for accurate diagnosis and treatment of kidney-related health conditions.

No Liability:
The developer of this software will not be held responsible for any decisions, misdiagnoses, or outcomes that may arise from using this tool. Any reliance on this software is solely at the user’s risk. It is essential to verify results with proper medical equipment and expertise.

Purpose of Development:
This software is developed purely for educational purposes, with the aim of demonstrating how AI and ML can be applied to the medical field and hospital systems. It is not designed for use in clinical settings or by the general public.

Avoid Misuse:
This application is restricted to trained professionals in hospitals and labs to ensure responsible use and avoid misuse by non-specialists. The misuse of such tools can lead to incorrect conclusions and potential harm, which is why this software is not intended for public access.

Encouragement for Healthcare Professionals:
This software aims to inspire healthcare professionals and researchers to further refine and advance AI-driven tools for medical diagnosis. Its purpose is to pave the way for future innovations in the field, rather than serve as a fully-fledged diagnostic tool.

By using this software, you acknowledge and agree to its limitations and the conditions outlined in this disclaimer. Always prioritize professional medical advice and institutional protocols over AI-generated predictions.
