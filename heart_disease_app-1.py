import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Page setup
st.set_page_config(page_title="Heart Health Check", page_icon="❤️", layout="wide")

# Clean styling
#st.markdown("""
 #    <style>
  #  .main {background: linear-gradient(to bottom right, #1a1a2e, #16213e, #0f3460);}
   # h1 {color: #e94560; text-align: center; font-size: 3em; margin-bottom: 10px;}
   # h2 {color: #00d4ff;}
    #h3 {color: #00d4ff;}
    #p {color: #00d4ff;}
    #.stButton>button {
     #   background: linear-gradient(90deg, #e94560, #ff6b9d);
      #  color: white;
       # font-size: 18px;
        #font-weight: bold;
        #padding: 12px 30px;
        #border-radius: 25px;
        #border: none;
        #transition: 0.3s;
    #}
    #.stButton>button:hover {transform: scale(1.05);}
    #</style>
    #""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    with open("heart_model.pkl","rb") as file:
       model = pickle.load(file)
    return model

model = load_model()

#Define function for prediction
def predict_heart_disease(inputs):
    prediction = model.predict([inputs])
    return prediction[0]

# Sidebar info
with st.sidebar:
    st.markdown("### 🤖 About This App")
    st.info("Uses machine learning to predict heart disease risk based on 29 key health indicators.")
    #st.metric("Model Accuracy", "90.24%")
    st.markdown("---")
    st.markdown("### 📌 Quick Guide")
    st.write("1. Fill in health details")
    st.write("2. Click predict")
    st.write("3. Get instant results")

# Input form
st.title("HEART DISEASE RISK PREDICTION APP")
st.markdown("Welcome to the **Heart Disease Prediction App**. This tool is designed to help you **assess your risk of heart disease** by analyzing key health and lifestyle indicators through a machine learning model. Simply fill in your details, and you will receive a prediction showing whether you are at **high or low risk** of developing heart disease.")
st.info("This app provides a data-driven risk estimate and is not a substitute for professional medical advice.")
st.markdown("### 📝 Enter your Health Details below:")
col1, col2, col3 = st.columns(3)

with col1:
    Age = st.number_input("Age (Years):", min_value = 18, max_value = 90)
    Sex = st.selectbox("Sex:", options= [0, 1], format_func=lambda x: "Female" if x == 0 else "Male", index = 1)
    Cholesterol = st.number_input("Cholesterol (mg/dL):", min_value = 120, max_value = 400)
    Heart = st.number_input("Heart Rate (bpm):", min_value = 40, max_value = 110)
    Diabetes = int(st.selectbox("Diabetes:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"))
    Family = int(st.selectbox("Family History:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"))
    Smoking = int(st.selectbox("Smoking:",options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"))
    Obesity = int(st.selectbox("Obesity:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"))
    Alcohol = int(st.selectbox("Alcohol Consumption:",options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"))
    Exercise = st.number_input("Exercise Hours Per Week (Hours/Week):", min_value = 0.002, max_value = 19.998)  

with col2:  
    Diet = st.selectbox("Diet:",options= [0, 1, 2], format_func = lambda x: ['Average', 'Healthly', 'Unhealthy'][x])
    Previous = int(st.selectbox("Previous Heart Problems:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"))
    Medication = int(st.selectbox("Medication Use:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes"))
    Level = st.number_input("Stress Level:", min_value = 1, max_value = 10)
    Sedentary = st.number_input("Sedentary Hours Per Day (Hours/Day):", min_value = 0.001, max_value = 11.999)
    Income = st.number_input("Income (USD/Year):", min_value = 20062, max_value = 299954)
    BMI= st.number_input("BMI (kg/m):", min_value = 18.00, max_value = 39.99)
    Triglycerides = st.number_input("Triglycerides (mg/dL):", min_value = 30, max_value = 800)
    Activity = st.number_input("Physical Activity Days Per Week (Days/Week):", min_value = 0, max_value = 7)
    Sleep = st.number_input("Sleep Hours Per Day (Hours/day):", min_value = 4, max_value = 10)

with col3:  
    Country = st.selectbox ('Country:', ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Colombia', 'France', 'Germany', 'India', 'Italy',
              'Japan', 'New Zealand', 'Nigeria', 'South Africa', 'South Korea', 'Spain' 'Thailand', 'United States', 'Vietnam'])
    #Attack = st.selectbox("Heart Attack #Risk:", options=[0, 1], format_func=lambda x: #"No" if x == 0 else "Yes")
    Systolic= st.number_input("Systolic Blood Pressure (mm Hg):", min_value = 90, max_value = 180)
    Diastolic = st.number_input("Diastolic Blood Pressure (mm Hg):", min_value = 60, max_value = 110)
    Stress = st.number_input("BMI Stress:", min_value = 18.00, max_value = 399.85)
    Ratio = st.number_input("Activity Ratio:", min_value = 0.0005, max_value = 19.1768)
    BP = st.number_input("Blood Presure Product mm Hg):", min_value = 5400, max_value = 19800)
    Interaction = st.number_input("Sleep Stress Interaction:", min_value = 4, max_value = 100)
    Substance = st.selectbox("Substance Use:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

#Prepare input data 
if st.button('Predict Heart Disease Risk'):
   st.title("Prediction Result:")
   inputs =[Age, Sex, Cholesterol, Heart, Diabetes, Family, Smoking, Obesity, Alcohol, Exercise]  
   inputs = np.asarray(inputs).reshape(1, -1)
   prediction = model.predict(inputs)
 
   if prediction == 1 :
      st.error("**HIGH RISK of Heart Disease! Please Consult a doctor immediately**")
      st.markdown("### Preventive Measures:")
      st.write("- Maintain a heart-healthy diet (low sodium, high fiber, low fat).")
      st.write("- Stop smoking and limit alcohol intake.")
      st.write("- Manage stress through relaxation or counseling.")
      st.write("- Increse physical activity under doctor supervision.")
      st.write("- Schedule regular checkups with a cardiologist.")
      st.write("- Take prescribed medications consistently and monitor vitals.")
   else:
      st.success("**LOW RISK of Heart Disease. Keep maintaining your healthy lifestyle!**")
      st.markdown("### Continue Healthy Routine:")
      st.write("- Continue eating a balanced and nutritious diet.")
      st.write("- Stay well hydrated daily.")
      st.write("- Maintain regular exercise habits.")
      st.write("- Avoid smoking and reduce alcohol.")
      st.write("- Get enough quality sleep every night.")
      st.write("- Keep stress levels low with rest and mindfulness.")

 #Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<p style='tet-align: center; color: #00d4ff;'>  Disclaimer: The model was trained on data using 8,763 patients, so it is not a reliable diagnostic tool. It is for educational purposes and should not replace professional medical advice.</p>", unsafe_allow_html=True)
