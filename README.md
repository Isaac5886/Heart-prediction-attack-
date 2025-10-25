# 🫀 Heart Attack Prediction Using Machine Learning

# 📌 Overview  
This project aims to predict the likelihood of a heart attack based on patient health indicators using various machine learning models. It covers data preprocessing, exploratory analysis, feature engineering, model building, evaluation, and optional deployment using Streamlit.

---

# 📂 Project Structure
```
├── data/                 # Dataset used
├── models/               # Saved models (.pkl)
├── notebooks/            # Jupyter Notebooks
├── app.py                # Streamlit app (for deployment)
├── requirements.txt      # Dependencies
└── README.md
```

---

# 🧠 Problem Statement  
Heart disease is a leading cause of death worldwide. Early prediction can help prevent fatal incidents. This project builds a machine learning model to classify whether an individual is at risk of a heart attack based on various health indicators.

---

📁 Dataset

The dataset contains *8,763* user records and *26 features*, sourced from [Kaggle](https://share.google/wOcbIlE09Nyk0fOzG). It includes both demographic and medical information used to predict heart attack risk.

*Key Features:*
- *Patient ID:* Unique identifier for each patient.

- *Age:* Age of the patient.

- *Sex:* Gender of the patient (Male/Female).

- *Cholesterol:* Cholesterol levels of the patient.

- *Blood Pressure:* Blood pressure of the patient (systolic/diastolic).

- Heart Rate: Heart rate of the patient.

- Diabetes: Whether the patient has diabetes (Yes/No).

- Family History: Family history of heart-related problems (1: Yes, 0: No).

- Smoking: Smoking status of the patient (1: Smoker, 0: Non-smoker).

- Obesity: Obesity status of the patient (1: Obese, 0: Not obese).

- Alcohol Consumption: Level of alcohol consumption by the patient (None/Light/Moderate/Heavy).

- Exercise Hours Per Week: Number of exercise hours per week.

- Diet: Dietary habits of the patient (Healthy/Average/Unhealthy).

- Previous Heart Problems: Previous heart problems of the patient (1: Yes, 0: No).

- Medication Use: Medication usage by the patient (1: Yes, 0: No).

- Stress Level: Stress level reported by the patient (1-10).

- Sedentary Hours Per Day: Hours of sedentary activity per day.

- Income: Income level of the patient.

- BMI: Body Mass Index (BMI) of the patient.

- Triglycerides: Triglyceride levels of the patient.

- Physical Activity Days Per Week: Days of physical activity per week.

- Sleep Hours Per Day: Hours of sleep per day.

- Country: Country of the patient.

- Continent: Continent where the patient resides.

- Hemisphere: Hemisphere where the patient resides.

- Heart Attack Risk (Outcome): Presence of heart attack risk (1: Yes, 0: No).

-----

# 🧼 Data Preprocessing  
- Handled missing values  
- Encoded categorical variables (e.g., `Sex`, `Diet`)  
- Applied feature scaling (`StandardScaler`)  
- Removed irrelevant features (e.g., `Patient ID`)  

---

# 📊 Exploratory Data Analysis (EDA)
- Distribution analysis (Age, Cholesterol, BMI, etc.)  
- Correlation heatmap to identify relationships  
- Outlier detection (boxplots)  
- Class distribution  

---

# ⚙️ Feature Engineering  
Created interaction and ratio-based features to enhance model performance:
- `BMI_Stress` = BMI × Stress Level  
- `Activity_Ratio` = Exercise Hours / (Sedentary Hours + 1)  
- `BP_Product` = Systolic × Diastolic BP  
- `Sleep_Stress_Interaction`  
- `Income_to_Medication`  
- `Smoking_Alcohol_Score`  

---

# ⚖️ SMOTE (Synthetic Oversampling)  
- Balanced the dataset using SMOTE to address class imbalance  
- Improved model generalization and recall on minority class  

---

# 🔍 Model Building & Hyperparameter Tuning  
Models trained with `GridSearchCV` and `StratifiedKFold` cross-validation:  
- Logistic Regression  
- Random Forest  
- LightGBM  
- CatBoost  
- MLP (Neural Network)  

---

# 📈  Evaluation Metrics  
Evaluated using multiple classification metrics:  
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  
- ROC-AUC Curve  

---

# 📊 Data Visualizations  
- KDE plots, boxplots, histograms  
- Correlation matrix heatmap  
- Count plots for categorical features  
- Feature importance plots (Random Forest, LightGBM, CatBoost)

# 🖥️ Deployment (Optional)  
- Deployed with *Streamlit* for interactive predictions  
- Docker-ready for containerized deployment  

# ▶️ How to Run the App
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

# ✅ Conclusion  
The trained models effectively predict heart attack risk, supporting medical professionals with early warning tools for diagnosis and preventive measures.

---

# 🚀 Future Improvements  
- Use larger and more diverse datasets  
- Incorporate clinical test results (e.g., ECG, CT scans)  
- Apply deep learning techniques (e.g., CNN on medical images)  
- Integrate into healthcare platforms for real-time predictions  

---

