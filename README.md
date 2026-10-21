# 🫀 Heart Disease Prediction System

A machine learning-powered web application built with **Streamlit** and **Scikit-Learn** that predicts the risk of cardiovascular disease based on clinical diagnostic metrics.

---

## 🌟 Live Demo

🔗 https://heart-disease-predictor-10vs.onrender.com

---

## 🚀 Key Features

- **Instant Risk Assessment:** Provides immediate prediction of heart disease risk using a trained Logistic Regression model.
- **Probability & Confidence Score:** Displays the percentage confidence behind each prediction.
- **Interactive Web Interface:** User-friendly UI featuring dual-column layouts, dropdown selectors, and sliders powered by Streamlit.
- **Cloud-Ready:** Deployed and publicly accessible on Render.

---

## 📊 Dataset & Clinical Features

The model analyzes 13 key physiological factors:

| Feature | Description | Range / Values |
| :--- | :--- | :--- |
| **`age`** | Age of the individual | Years |
| **`sex`** | Biological sex | `0` = Female, `1` = Male |
| **`cp`** | Chest Pain Type | `0` = Typical Angina, `1` = Atypical Angina, `2` = Non-anginal, `3` = Asymptomatic |
| **`trestbps`** | Resting blood pressure | mm Hg (at hospital admission) |
| **`chol`** | Serum cholesterol | mg/dl |
| **`fbs`** | Fasting blood sugar > 120 mg/dl | `0` = False, `1` = True |
| **`restecg`** | Resting electrocardiographic results | `0` = Normal, `1` = ST-T Wave Abnormality, `2` = LV Hypertrophy |
| **`thalach`** | Maximum heart rate achieved | bpm |
| **`exang`** | Exercise-induced angina | `0` = No, `1` = Yes |
| **`oldpeak`** | ST depression induced by exercise | Relative to rest (numerical) |
| **`slope`** | Peak exercise ST segment slope | `0` = Upsloping, `1` = Flat, `2` = Downsloping |
| **`ca`** | Major vessels colored by fluoroscopy | 0 to 4 |
| **`thal`** | Thalassemia | `1` = Normal, `2` = Fixed Defect, `3` = Reversible Defect |

---

## 🛠️ Tech Stack

- **Language:** Python
- **Machine Learning:** Scikit-Learn (Logistic Regression)
- **Data Manipulation:** Pandas, NumPy
- **Web Framework:** Streamlit
- **Deployment Platform:** Render
- **Version Control:** Git & GitHub

---

<img width="1568" height="915" alt="image" src="https://github.com/user-attachments/assets/25204cf0-0388-4ed2-a2b2-21e1f176d4ca" />


## ⚙️ Local Setup and Installation

Follow these steps to run the application locally on your computer:

### 1. Clone the repository
```bash
git clone [https://github.com/RKO619-Drew/heart-disease-predictor.git](https://github.com/RKO619-Drew/heart-disease-predictor.git)
cd heart-disease-predictor

