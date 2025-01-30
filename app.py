import streamlit as st
import pandas as pd
import numpy as np
import joblib
import webbrowser
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder

# Load dataset
df = pd.read_csv("ObesityDataSet.csv")

# Encoding categorical variables
encoder_dict = {
    'Gender': OrdinalEncoder(categories=[['Female', 'Male']]),
    'family_history_with_overweight': OrdinalEncoder(categories=[['no', 'yes']]),
    'FAVC': OrdinalEncoder(categories=[['no', 'yes']]),
    'SMOKE': OrdinalEncoder(categories=[['no', 'yes']]),
    'SCC': OrdinalEncoder(categories=[['no', 'yes']]),
    'CAEC': OrdinalEncoder(categories=[['no', 'Sometimes', 'Frequently', 'Always']]),
    'CALC': OrdinalEncoder(categories=[['no', 'Sometimes', 'Frequently', 'Always']]),
    'MTRANS': OrdinalEncoder(categories=[['Walking', 'Bike', 'Motorbike', 'Public_Transportation', 'Automobile']]),
    'NObeyesdad': OrdinalEncoder(categories=[['Insufficient_Weight', 'Normal_Weight', 'Overweight_Level_I', 'Overweight_Level_II', 'Obesity_Type_I',
                                              'Obesity_Type_II', 'Obesity_Type_III']])
}

for col, encoder in encoder_dict.items():
    df[[col]] = encoder.fit_transform(df[[col]])

# Split features and target
X = df.drop('NObeyesdad', axis=1)
y = df['NObeyesdad']

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, 'obesity_model.pkl')

# Load model
model = joblib.load('obesity_model.pkl')

def predict_obesity(data):
    input_data = np.array(data).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.set_page_config(page_title="BodyCheck+", layout="wide")

# Sidebar
st.sidebar.image("logo.png", use_container_width=True)
st.sidebar.header("BodyCheck+")
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Artikel kesehatan di sidebar
if st.sidebar.button("Health Articles"):
    webbrowser.open("https://www.healthline.com/nutrition")

# Prediksi Tingkat Obesitas
st.title("Obesity Level Prediction")
st.markdown("<hr>", unsafe_allow_html=True)
st.write("Enter your data to predict your obesity level:")

# Input Nama
name = st.text_input("Enter Your Name:")

# Jika belum mengisi nama, hentikan proses
if not name:
    st.warning("Please enter your name first to continue.")
    st.stop()

# Input data
gender = st.selectbox("Enter Your Gender:", ['Female', 'Male'])
age = st.number_input("Enter Your Age:", min_value=1, max_value=100, value=25)
height = st.number_input("Enter Your Height (cm):", min_value=100, max_value=250, value=170)
weight = st.number_input("Enter Your Weight (kg):", min_value=30, max_value=200, value=70)
family_history = st.selectbox("Do You Have a Family History of Obesity?", ['no', 'yes'])
favc = st.selectbox("Do You Frequently Eat High-Calorie Foods?", ['no', 'yes'])
fcvc = st.slider("Enter Your Vegetable Consumption Frequency:", min_value=1.0, max_value=3.0, value=2.0)
ncp = st.slider("Enter the Number of Meals You Eat per Day:", min_value=1, max_value=5, value=3)
caec = st.selectbox("Enter Your Snacking Habit:", ['no', 'Sometimes', 'Frequently', 'Always'])
smoke = st.selectbox("Do You Smoke?", ['no', 'yes'])
ch2o = st.slider("Enter Your Daily Water Intake (Liters):", min_value=1.0, max_value=3.0, value=2.0)
scc = st.selectbox("Do You Monitor Your Calorie Intake?", ['no', 'yes'])
faf = st.slider("Enter Your Weekly Physical Activity Frequency:", min_value=0, max_value=5, value=2)
tue = st.slider("Enter Your Daily Screen Time (Hours):", min_value=0.0, max_value=10.0, value=2.0)
calc = st.selectbox("Enter Your Alcohol Consumption Frequency:", ['no', 'Sometimes', 'Frequently', 'Always'])
mtrans = st.selectbox("Enter Your Main Mode of Transportation:", ['Walking', 'Bike', 'Motorbike', 'Public_Transportation', 'Automobile'])

# Encoding user input
user_data = [
    encoder_dict['Gender'].transform([[gender]])[0][0],
    age, height, weight,
    encoder_dict['family_history_with_overweight'].transform([[family_history]])[0][0],
    encoder_dict['FAVC'].transform([[favc]])[0][0],
    fcvc, ncp,
    encoder_dict['CAEC'].transform([[caec]])[0][0],
    encoder_dict['SMOKE'].transform([[smoke]])[0][0],
    ch2o,
    encoder_dict['SCC'].transform([[scc]])[0][0],
    faf, tue,
    encoder_dict['CALC'].transform([[calc]])[0][0],
    encoder_dict['MTRANS'].transform([[mtrans]])[0][0]
]

# Tombol Prediksi
if st.button("Predict"):
    prediction = predict_obesity(user_data)
    result_label = encoder_dict['NObeyesdad'].categories[0][int(prediction)]
    st.success(f"{name}, your predicted obesity level is {result_label}")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Simpan laporan prediksi ke session state
    st.session_state["report_text"] = f"""
Hi {name}, Today, you will have a clearer picture of yourself! You are a {gender} aged {age} years, with a height of {height} cm and weight of {weight} kg. In your daily life, you are used to consuming about {ch2o} liters of water each day, which is essential for maintaining body hydration.

Additionally, your snacking habits are categorized as "{caec}", which can impact your eating patterns and overall health. Not only that, your alcohol consumption pattern is recorded as "{calc}", which can also affect your metabolism and long-term well-being.

In terms of activity, the way you travel daily also provides important insights. Your primary mode of transportation is "{mtrans}", which can contribute to the level of physical activity you engage in each day.

Based on various lifestyle factors you follow, our system has analyzed and estimated that your potential obesity level is {result_label}.

Knowing this condition is a great first step! With this insight, you can start making wiser decisions for your health moving forward.
   """

    # Tombol unduh laporan prediksi muncul setelah prediksi dilakukan
    st.sidebar.download_button(label="Prediction Report",
                               data=st.session_state["report_text"],
                               file_name="Prediction_Report.txt",
                               mime="text/plain",
                               key="download_report_after_prediction")

# Tombol Tentang Kami di sidebar
if st.sidebar.button("About Us"):
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("About Us")
    st.write("""
    **BodyCheck+** is an obesity level prediction app designed to help users understand their potential obesity level based on various lifestyle and health factors.
    The app leverages machine learning algorithms to provide personalized predictions, assisting users in making informed decisions regarding their health.
    
    Our goal is to support individuals in achieving healthier lifestyles by raising awareness about factors that may influence obesity risks. With user-friendly features and comprehensive health data analysis, BodyCheck+ aims to be a reliable tool in your journey toward better health.
    
    Whether you're looking to maintain a healthy weight, prevent obesity, or make changes to your daily habits, BodyCheck+ is here to guide you through the process with practical insights and actionable recommendations.
    """)


st.caption('Copyright(c) BodyCheck+')