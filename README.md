# 🎓 Student Marks Prediction Model

A Machine Learning based application that predicts students' marks based on their daily study hours.

This project uses a trained regression model to estimate marks and demonstrates how Machine Learning can be used for educational data prediction.

## 🚀 Features

- Predicts student marks based on study hours
- Simple and interactive user interface
- Uses a trained Machine Learning regression model
- Provides quick predictions

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

## 🤖 Machine Learning Model

- Algorithm: Random Forest Regression
- Problem Type: Regression
- Input Feature:
  - Daily Study Hours

- Output:
  - Predicted Marks

## 📦 Requirements

Before running this project, make sure you have:

- Python 3.14.5
- Required Python libraries

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## 📂 Project Files

This repository contains:

- `app.py` — Streamlit application
- `studentmarksmodel.joblib` — Trained Machine Learning model
- `requirements.txt` — Required Python packages

## ▶️ How to Run

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Keep Files Together

Make sure `app.py` and `studentmarksmodel.joblib` are in the same folder.

### 3. Run Streamlit Application

Open terminal in the project folder and run:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## 🎯 Project Purpose

The purpose of this project is to predict student performance using Machine Learning and deploy the trained model as a real-world application using Streamlit.

