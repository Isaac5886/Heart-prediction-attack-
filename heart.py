import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Page configuration
st.set_page_config(
    page_title="Heart Disease Risk Assessment",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional styling
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #1e3a8a;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 600;
        padding-bottom: 10px;
        border-bottom: 3px solid #3b82f6;
    }
    h2 {
        color: #1e40af;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 500;
    }
    h3 {
        color: #2563eb;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        font-size: 16px;
        font-weight: 600;
        padding: 14px 40px;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }
    .info-box {
        background-color: #eff6ff;
        padding: 20px;
        border-radius: 8px;
        border-left: 4px solid #3b82f6;
        margin: 20px 0;
    }
    .metric-card {
        background: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    try:
    with open("heart_model.pkl", "rb") as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("⚠️ Failed to load model:{e}")
        return None

model = load_model()

# Professional sidebar
with st.sidebar:
    #st.image("https://img.icons8.com/color/96/000000/heartbeat.png", width=80)
    st.markdown("## 📊 Clinical Decision Support")
    st.markdown("---")
    
    st.markdown("### About This Tool")
    st.markdown("""
    This clinical decision support system utilizes advanced machine learning 
    algorithms to assess cardiovascular disease risk based on comprehensive 
    patient health metrics and lifestyle factors.
    """)
    
    st.markdown("---")
    st.markdown("### 🔬 Model Information")
    st.markdown("""
    - **Training Dataset:** 8,763 patient records
    - **Features Analyzed:** 29 clinical indicators
    - **Purpose:** Risk stratification & screening
    """)
    
    st.markdown("---")
    st.markdown("### 📋 Assessment Process")
    st.markdown("""
    1. **Input Data:** Complete all patient information fields
    2. **Validation:** System validates data integrity
    3. **Analysis:** ML model processes health indicators
    4. **Results:** Receive risk assessment with recommendations
    """)
    
    st.markdown("---")
    st.markdown("### ⚕️ Important Notice")
    st.warning("""
    This tool is designed for educational and screening purposes only. 
    It does not replace professional medical diagnosis or clinical judgment.
    """)

# Header section
st.title("🫀 Cardiovascular Disease Risk Assessment System")
st.markdown("---")

# Introduction
st.markdown("""
<div class="info-box">
<h3>Welcome to the Professional Heart Health Assessment Platform</h3>
<p>This evidence-based risk assessment tool employs machine learning methodology to evaluate 
cardiovascular disease probability through comprehensive analysis of clinical parameters, 
lifestyle factors, and patient demographics. The system provides data-driven insights to 
support early detection and preventive care strategies.</p>
</div>
""", unsafe_allow_html=True)

st.info("📌 **Note:** All information provided is confidential and used solely for risk calculation purposes.")

# Input form section
st.markdown("---")
st.markdown("## 📝 Patient Information & Clinical Data Entry")
st.markdown("Please provide accurate information for all fields to ensure optimal assessment accuracy.")

# Create tabs for organized input
tab1, tab2, tab3, tab4 = st.tabs(["👤 Demographics & Vitals", "🧬 Medical History", "💊 Lifestyle Factors", "🔬 Laboratory Values"])

# Initialize variables
with tab1:
    st.markdown("### Basic Patient Information")
    col1, col2 = st.columns(2)
    
    with col1:
        Age = st.number_input("Age (years)", min_value=18, max_value=90, value=45, help="Patient's current age in years")
        Sex = st.selectbox("Biological Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male", index=1)
        BMI = st.number_input("Body Mass Index (kg/m²)", min_value=18.00, max_value=39.99, value=25.0, format="%.2f", 
                            help="Weight in kg divided by height in meters squared")
        Country = st.selectbox('Country of Residence', [
            'Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Colombia', 
            'France', 'Germany', 'India', 'Italy', 'Japan', 'New Zealand', 
            'Nigeria', 'South Africa', 'South Korea', 'Spain', 'Thailand', 
            'United States', 'Vietnam'
        ])
    
    with col2:
        Systolic = st.number_input("Systolic Blood Pressure (mmHg)", min_value=90, max_value=180, value=120, 
                                  help="Upper blood pressure reading")
        Diastolic = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=60, max_value=110, value=80,
                                   help="Lower blood pressure reading")
        Heart = st.number_input("Resting Heart Rate (bpm)", min_value=40, max_value=110, value=70,
                              help="Beats per minute at rest")
        Income = st.number_input("Annual Income (USD)", min_value=20062, max_value=299954, value=60000,
                               help="Socioeconomic indicator")

with tab2:
    st.markdown("### Medical History & Risk Factors")
    col1, col2 = st.columns(2)
    
    with col1:
        Diabetes = st.selectbox("Diabetes Mellitus", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes",
                               help="History of diabetes diagnosis")
        Family = st.selectbox("Family History of Heart Disease", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes",
                            help="First-degree relatives with cardiovascular disease")
        Previous = st.selectbox("Previous Cardiac Events", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes",
                              help="History of heart attack, angina, or cardiac procedures")
        Obesity = st.selectbox("Clinical Obesity", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes",
                             help="BMI ≥ 30 kg/m² or clinical diagnosis")
    
    with col2:
        Medication = st.selectbox("Current Cardiac Medications", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes",
                                help="Taking medications for heart/blood pressure")
        Attack = st.selectbox("High Heart Attack Risk (Clinical Assessment)", options=[0, 1], 
                            format_func=lambda x: "No" if x == 0 else "Yes")
        Substance = st.selectbox("Substance Use History", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes",
                               help="History of drug use affecting cardiovascular health")

with tab3:
    st.markdown("### Lifestyle & Behavioral Factors")
    col1, col2 = st.columns(2)
    
    with col1:
        Smoking = st.selectbox("Smoking Status", options=[0, 1], format_func=lambda x: "Non-Smoker" if x == 0 else "Current/Former Smoker")
        Alcohol = st.selectbox("Alcohol Consumption", options=[0, 1], format_func=lambda x: "No/Minimal" if x == 0 else "Regular Use",
                             help="Regular alcohol consumption")
        Diet = st.selectbox("Diet Quality", options=[0, 1, 2], format_func=lambda x: ['Average', 'Healthy', 'Unhealthy'][x],
                          help="Overall dietary pattern assessment")
        Exercise = st.number_input("Exercise Hours Per Week", min_value=0.0, max_value=20.0, value=3.0, step=0.5,
                                 help="Moderate to vigorous physical activity")
    
    with col2:
        Activity = st.number_input("Physical Activity Days Per Week", min_value=0, max_value=7, value=3,
                                 help="Days with ≥30 minutes of activity")
        Sedentary = st.number_input("Sedentary Hours Per Day", min_value=0.0, max_value=12.0, value=6.0, step=0.5,
                                   help="Hours spent sitting/inactive")
        Sleep = st.number_input("Average Sleep Hours Per Day", min_value=4, max_value=10, value=7,
                              help="Average nightly sleep duration")
        Level = st.number_input("Stress Level (1-10 scale)", min_value=1, max_value=10, value=5,
                              help="Self-reported stress assessment")

with tab4:
    st.markdown("### Laboratory Values & Calculated Metrics")
    col1, col2 = st.columns(2)
    
    with col1:
        Cholesterol = st.number_input("Total Cholesterol (mg/dL)", min_value=120, max_value=400, value=200,
                                    help="Total serum cholesterol")
        Triglycerides = st.number_input("Triglycerides (mg/dL)", min_value=30, max_value=800, value=150,
                                      help="Serum triglyceride level")
        BP = st.number_input("Blood Pressure Product (mmHg)", min_value=5400, max_value=19800, value=9600,
                           help="Systolic × Diastolic (calculated metric)")
    
    with col2:
        Stress = st.number_input("BMI-Stress Index", min_value=18.00, max_value=399.85, value=125.0, format="%.2f",
                               help="Composite stress-BMI metric")
        Ratio = st.number_input("Activity-to-Sedentary Ratio", min_value=0.0, max_value=20.0, value=0.5, step=0.1,
                              help="Physical activity divided by sedentary time")
        Interaction = st.number_input("Sleep-Stress Interaction Score", min_value=4, max_value=100, value=35,
                                    help="Sleep hours × stress level")

# Prediction section
st.markdown("---")
st.markdown("## 🔍 Risk Assessment Analysis")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔬 Generate Risk Assessment Report", use_container_width=True, type="primary")

if predict_button:
    if model is None:
        st.error("❌ Model not loaded. Cannot perform assessment.")
    else:
        with st.spinner("🔄 Analyzing patient data and computing risk scores..."):
            # Prepare all 29 features
            country_encoded = ['Argentina', 'Australia', 'Brazil', 'Canada', 'China', 'Colombia', 
                             'France', 'Germany', 'India', 'Italy', 'Japan', 'New Zealand', 
                             'Nigeria', 'South Africa', 'South Korea', 'Spain', 'Thailand', 
                             'United States', 'Vietnam'].index(Country)
            
            inputs = [
                Age, Sex, Cholesterol, Heart, Diabetes, Family, Smoking, Obesity, 
                Alcohol, Exercise
            ]
            
            inputs_array = np.array(inputs).reshape(1, -1)
            
            try:
                prediction = model.predict(inputs_array)
                
                # Get probability scores if available
                try:
                    probability = model.predict_proba(inputs_array)[0]
                    low_risk_prob = probability[0] * 100
                    high_risk_prob = probability[1] * 100
                    has_probability = True
                except AttributeError:
                    # Model doesn't support predict_proba
                    has_probability = False
                    low_risk_prob = 0
                    high_risk_prob = 0
                
                st.markdown("---")
                st.markdown("## 📊 Assessment Results")
                
                # Display probability metrics if available
                if has_probability:
                    st.markdown("### 📈 Risk Probability Scores")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric(
                            label="Low Risk Probability",
                            value=f"{low_risk_prob:.1f}%",
                            delta=None
                        )
                    
                    with col2:
                        st.metric(
                            label="High Risk Probability",
                            value=f"{high_risk_prob:.1f}%",
                            delta=None
                        )
                    
                    with col3:
                        confidence = max(low_risk_prob, high_risk_prob)
                        st.metric(
                            label="Model Confidence",
                            value=f"{confidence:.1f}%",
                            delta=None
                        )
                    
                    # Visual probability bar
                    st.markdown("#### Risk Distribution")
                    st.progress(high_risk_prob / 100)
                    st.caption(f"Risk Spectrum: {low_risk_prob:.1f}% Low Risk ← → {high_risk_prob:.1f}% High Risk")
                    st.markdown("---")

                
                st.markdown("---")
                st.markdown("## 📊 Assessment Results")
                
                if prediction[0] == 1:
                    st.markdown("""
                    <div style='background-color: #fef2f2; padding: 30px; border-radius: 10px; border-left: 6px solid #dc2626;'>
                        <h2 style='color: #dc2626; margin-top: 0;'>⚠️ HIGH CARDIOVASCULAR RISK DETECTED</h2>
                        <p style='font-size: 16px; color: #7f1d1d;'>
                        The risk assessment model has identified a <strong>high probability</strong> of cardiovascular disease 
                        based on the provided clinical and lifestyle data. <strong>Immediate medical consultation is strongly recommended.</strong>
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("### 🏥 Recommended Clinical Actions")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("""
                        **Immediate Steps:**
                        - 🩺 Schedule comprehensive cardiac evaluation
                        - 📋 Complete full lipid panel and cardiac biomarkers
                        - 💊 Review and optimize medication regimen
                        - 📊 Baseline ECG and stress testing
                        - 🔬 Consider advanced cardiac imaging if indicated
                        """)
                    
                    with col2:
                        st.markdown("""
                        **Lifestyle Interventions:**
                        - 🥗 Adopt DASH or Mediterranean diet
                        - 🚭 Immediate smoking cessation support
                        - 🏃‍♂️ Supervised cardiac rehabilitation program
                        - 😌 Stress management and mental health support
                        - 💤 Sleep hygiene optimization
                        """)
                    
                    st.markdown("### 📈 Monitoring Protocol")
                    st.markdown("""
                    - **Follow-up Frequency:** Every 3-6 months or as directed by cardiologist
                    - **Key Metrics to Track:** Blood pressure, cholesterol, weight, physical activity
                    - **Emergency Signs:** Chest pain, shortness of breath, palpitations, unusual fatigue
                    """)
                    
                else:
                    st.markdown("""
                    <div style='background-color: #f0fdf4; padding: 30px; border-radius: 10px; border-left: 6px solid #16a34a;'>
                        <h2 style='color: #16a34a; margin-top: 0;'>✅ LOW CARDIOVASCULAR RISK</h2>
                        <p style='font-size: 16px; color: #14532d;'>
                        The assessment indicates a <strong>low probability</strong> of cardiovascular disease based on 
                        current health metrics. Continue maintaining healthy lifestyle practices and regular health monitoring.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("### 💚 Preventive Health Maintenance")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("""
                        **Continue Current Practices:**
                        - ✅ Maintain balanced, nutrient-rich diet
                        - ✅ Regular cardiovascular exercise routine
                        - ✅ Consistent sleep schedule (7-9 hours)
                        - ✅ Stress management techniques
                        - ✅ Avoid tobacco and limit alcohol
                        """)
                    
                    with col2:
                        st.markdown("""
                        **Routine Monitoring:**
                        - 📅 Annual health check-ups
                        - 🩺 Blood pressure monitoring
                        - 📊 Lipid panel every 2-5 years
                        - ⚖️ Maintain healthy weight
                        - 🏃 Stay physically active
                        """)
                    
                    st.markdown("### 🎯 Optimization Opportunities")
                    st.info("""
                    Even with low risk, there's always room for improvement. Consider:
                    - Increasing physical activity if below recommended levels
                    - Further dietary improvements (more vegetables, whole grains)
                    - Enhanced stress reduction techniques (meditation, yoga)
                    - Building strong social connections for mental health
                    """)
                
                # General recommendations
                st.markdown("---")
                st.markdown("### 📚 Evidence-Based Resources")
                st.markdown("""
                - **American Heart Association:** Heart-healthy living guidelines
                - **CDC Heart Disease Prevention:** www.cdc.gov/heartdisease
                - **National Heart, Lung, and Blood Institute:** Educational materials
                - **Local Cardiac Rehabilitation Programs:** Contact your healthcare provider
                """)
                
            except Exception as e:
                st.error(f"❌ Error during risk assessment: {str(e)}")
                st.info("Please verify all input fields are completed correctly and try again.")

# Footer
st.markdown("---")
st.markdown("""
<div style='background-color: #eff6ff; padding: 25px; border-radius: 8px; margin-top: 30px;'>
    <h3 style='color: #1e40af; margin-top: 0;'>⚕️ Medical Disclaimer & Important Information</h3>
    <p style='color: #1e3a8a; line-height: 1.6;'>
    <strong>This risk assessment tool is intended for educational and screening purposes only.</strong> 
    The predictive model was developed using a dataset of 8,763 patient records and analyzes 29 clinical 
    indicators. However, this system does <strong>NOT</strong> constitute medical diagnosis, treatment advice, 
    or a substitute for professional healthcare consultation.
    </p>
    <p style='color: #1e3a8a; line-height: 1.6;'>
    <strong>Clinical Limitations:</strong> Machine learning models have inherent limitations and may not 
    account for all individual factors. Risk predictions should be interpreted by qualified healthcare 
    professionals in the context of complete medical history, physical examination, and additional diagnostic testing.
    </p>
    <p style='color: #1e3a8a; line-height: 1.6;'>
    <strong>Action Required:</strong> If you have concerns about your cardiovascular health, experience 
    symptoms, or receive a high-risk assessment, please consult with a licensed healthcare provider immediately. 
    In case of emergency (chest pain, difficulty breathing), call emergency services (911 in US).
    </p>
    <hr style='border: 1px solid #93c5fd; margin: 15px 0;'>
    <p style='color: #1e40af; text-align: center; margin-bottom: 0; font-size: 14px;'>
    © 2025 Heart Disease Risk Assessment System | For Healthcare Professional & Educational Use
    </p>
</div>
""", unsafe_allow_html=True)
