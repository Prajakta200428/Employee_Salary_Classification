# 💼Employee_Salary_Classification Using Machine Learning

This project predicts whether a person earns more than 50,000 per year based on demographic and employment information using various machine learning models. A Streamlit web application is also developed for real-time predictions.

## 📌 Problem Statement

The aim of this project is to build a machine learning model that can classify individuals into two income groups: `<=50K` and `>50K`. The model uses features like age, education, occupation, and work hours. The final solution includes a user-friendly web app that allows users to input details and get instant salary group predictions.

## 🧠 Machine Learning Models, 🔄 Workflow, and 📊 Features

This project uses a complete machine learning pipeline including model comparison and deployment. The steps and models used are as follows:

**Machine Learning Models**
- Logistic Regression
- Random Forest
- Gradient Boosting Classifier
- Histogram-based Gradient Boosting
- MLPClassifier (Neural Network)
- LightGBM
- CatBoost

✅ **LightGBM** showed the best accuracy and was selected for the final deployment.

**Workflow Overview**
1. Data loading from CSV
2. Data preprocessing:
   - Handling missing and ambiguous values
   - Replacing unclear categories (e.g., '?')
   - Removing outliers using the IQR method
   - Label encoding for categorical variables
3. Splitting dataset (80% training, 20% testing)
4. Model training with multiple algorithms
5. Evaluation of all models to choose the best
6. Saving the best model using `joblib`
7. Streamlit frontend development
8. Ngrok tunnel for deployment and external access

**Features Used**
- Age
- Education
- Workclass
- Occupation
- Marital Status
- Relationship
- Race
- Sex
- Hours per Week
- Capital Gain
- Capital Loss
- Native Country

## 🚀 Deployment

To deploy the application locally and make it accessible on the web:

1. Launch the Streamlit app:
streamlit run app.py

2.Open a Public Tunnel Using Ngrok
To make your Streamlit app accessible on the internet, use Ngrok:
ngrok config add-authtoken <your_auth_token>
ngrok http 8501

