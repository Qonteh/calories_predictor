import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('calorie_predictor_model.pkl')

# Streamlit page config
st.set_page_config(page_title="Calorie Predictor", page_icon="🔥", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f7f7f7;
            color: #333;
        }
        .header {
            text-align: center;
            color: #2c3e50;
            font-size: 3em;
            font-weight: bold;
        }
        .subheader {
            text-align: center;
            color: #16a085;
            font-size: 1.5em;
            margin-top: -10px;
        }
        .sidebar {
            background-color: #16a085;
            color: white;
            padding: 2rem;
        }
        .predict-button {
            background-color: #16a085;
            color: white;
            font-size: 1.2em;
            width: 100%;
            height: 40px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }
        .predict-button:hover {
            background-color: #1abc9c;
        }
        .output {
            font-size: 1.5em;
            color: #e74c3c;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Header and Subheader
st.markdown("<div class='header'>Calorie Needs Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Estimate Your Daily Calorie Requirement 🔥</div>", unsafe_allow_html=True)

# Sidebar inputs
st.sidebar.title("Input Details")
st.sidebar.markdown("Fill in your personal information")

# Input fields (Styling from sidebar)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
age = st.sidebar.slider("Age", 10, 80, 25)
daily_meals = st.sidebar.selectbox("Meals per Day", [1, 2, 3, 4])
physical_exercise = st.sidebar.selectbox("Exercise Level", ["None", "Low", "Moderate", "High"])
height = st.sidebar.slider("Height (cm)", 100, 220, 170)
weight = st.sidebar.slider("Weight (kg)", 30, 150, 70)
bmr = st.sidebar.number_input("BMR", min_value=500.0, max_value=4000.0, value=1500.0)
carbs = st.sidebar.number_input("Carbohydrates (g)", min_value=0.0, max_value=600.0, value=250.0)
proteins = st.sidebar.number_input("Proteins (g)", min_value=0.0, max_value=300.0, value=100.0)
fats = st.sidebar.number_input("Fats (g)", min_value=0.0, max_value=200.0, value=70.0)

# Convert inputs to numerical
gender_num = 1 if gender == "Male" else 0
exercise_map = {"None": 0, "Low": 1, "Moderate": 2, "High": 3}
exercise_num = exercise_map[physical_exercise]

# Predict button
predict_button = st.sidebar.button("Predict Calories 🔍", key="predict")

# Output
if predict_button:
    user_input = np.array([[gender_num, age, daily_meals, exercise_num, height, weight, bmr, carbs, proteins, fats]])
    prediction = model.predict(user_input)
    
    # Output Prediction
    st.markdown("<div class='output'>Your Estimated Daily Calories: <b>{:.2f} kcal</b></div>".format(prediction[0]), unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <img src="https://www.freeiconspng.com/uploads/healthy-food-icon-10.png" alt="Calorie" width="200"/>
    </div>
    """, unsafe_allow_html=True)

