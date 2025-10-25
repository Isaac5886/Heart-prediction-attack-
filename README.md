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

