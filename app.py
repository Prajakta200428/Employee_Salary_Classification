import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("best_model.pkl")



# Label encoders used in training — must match exactly!
education_map = {
    "Bachelors": 0, "Masters": 1, "PhD": 2, "HS-grad": 3,
    "Assoc": 4, "Some-college": 5
}
marital_map = {
    "Never-married": 0, "Married": 1, "Divorced": 2,
    "Separated": 3, "Widowed": 4
}
occupation_map = {
    "Tech-support": 0, "Craft-repair": 1, "Other-service": 2, "Sales": 3,
    "Exec-managerial": 4, "Prof-specialty": 5, "Handlers-cleaners": 6,
    "Machine-op-inspct": 7, "Adm-clerical": 8, "Farming-fishing": 9,
    "Transport-moving": 10, "Priv-house-serv": 11,
    "Protective-serv": 12, "Armed-Forces": 13
}
workclass_map = {
    "Private": 0, "Self-emp-not-inc": 1, "Self-emp-inc": 2,
    "Federal-gov": 3, "Local-gov": 4, "State-gov": 5,
    "Without-pay": 6, "Never-worked": 7
}
relationship_map = {
    "Husband": 0, "Wife": 1, "Own-child": 2,
    "Not-in-family": 3, "Unmarried": 4, "Other-relative": 5
}
country_map = {
    "United-States": 0, "India": 1, "Mexico": 2,
    "Philippines": 3, "Germany": 4, "Canada": 5,
    "China": 6, "England": 7
}
sex_map = {
    "Male": 0, "Female": 1
}
race_map = {
    "White": 0, "Black": 1, "Asian-Pac-Islander": 2,
    "Amer-Indian-Eskimo": 3, "Other": 4
}

# Streamlit UI
st.set_page_config(page_title="Employee Salary Classifier", page_icon="📊", layout="wide")

st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        h1 { color: #003366; }
        .subheader { color: #444; font-size: 17px; }
        .stButton > button {
            background-color: #004080;
            color: white;
            border-radius: 6px;
        }
        .stButton > button:hover {
            background-color: #0059b3;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>📊 Employee Salary Classification</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader' style='text-align: center;'>Predict whether an employee earns >50K or ≤50K</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 18, 65, 30)
    education = st.selectbox("Education Level", list(education_map.keys()))
    marital_status = st.selectbox("Marital Status", list(marital_map.keys()))
    race = st.selectbox("Race", list(race_map.keys()))

with col2:
    occupation = st.selectbox("Occupation", list(occupation_map.keys()))
    workclass = st.selectbox("Work Class", list(workclass_map.keys()))
    relationship = st.selectbox("Relationship", list(relationship_map.keys()))
    sex = st.selectbox("Sex", list(sex_map.keys()))

with col3:
    experience = st.slider("Years of Experience", 0, 40, 5)
    hours_per_week = st.slider("Hours per Week", 1, 80, 40)
    capital_gain = st.number_input("Capital Gain", 0, 99999, 0)
    capital_loss = st.number_input("Capital Loss", 0, 99999, 0)
    native_country = st.selectbox("Country", list(country_map.keys()))

# Build input DataFrame
input_df = pd.DataFrame({
    'age': [age],
    'education': [education_map[education]],
    'marital-status': [marital_map[marital_status]],
    'occupation': [occupation_map[occupation]],
    'workclass': [workclass_map[workclass]],
    'relationship': [relationship_map[relationship]],
    'sex': [sex_map[sex]],
    'race': [race_map[race]],
    'capital-gain': [capital_gain],
    'capital-loss': [capital_loss],
    'native-country': [country_map[native_country]],
    'experience': [experience],
    'hours-per-week': [hours_per_week]
})

st.markdown("#### 📊 Input Summary")
st.dataframe(input_df)

# Predict
if st.button("🚀 Predict Salary Class"):
    try:
        prediction = model.predict(input_df)
        st.success(f"✅ Prediction: `{prediction[0]}`")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

