# 🏭 Manufacturing Equipment Output Prediction using Linear Regression

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?logo=numpy)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

This project predicts the **hourly production output (Parts Per Hour)** of an injection molding machine using **Linear Regression**.

The prediction is based on various machine operating parameters such as:

- 🌡 Injection Temperature
- ⚙ Injection Pressure
- ⏱ Cycle Time
- ❄ Cooling Time
- 🧪 Material Viscosity
- 🌍 Ambient Temperature
- 🔧 Machine Age
- 👨‍🏭 Operator Experience
- 🛠 Maintenance Hours
- 🌞 Shift
- 🏭 Machine Type
- 📦 Material Grade
- 📅 Day of Week
- 📊 Efficiency Score
- 📈 Machine Utilization

The trained model is deployed using **FastAPI** and containerized with **Docker**.

---

# 🎯 Problem Statement

Manufacturing industries need to optimize production efficiency while maintaining product quality.

This project predicts **Parts Per Hour** using machine operating parameters, helping production teams:

- Improve production planning
- Optimize machine settings
- Detect underperforming machines
- Increase operational efficiency

---

# 🚀 Features

✅ Data Cleaning

✅ Missing Value Handling

✅ Exploratory Data Analysis (EDA)

✅ Feature Scaling

✅ One-Hot Encoding

✅ Linear Regression Model

✅ Model Evaluation

✅ FastAPI Deployment

✅ Docker Containerization

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| API | FastAPI |
| Deployment | Uvicorn |
| Containerization | Docker |

---

# 📂 Dataset Information

- Dataset Size: **1000 Samples**
- Features: **17**
- Target Variable:
  - Parts_Per_Hour

Missing values were handled using Median Imputation.

Categorical variables were encoded using One-Hot Encoding.

Numerical variables were standardized using StandardScaler.

---

# 📊 Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
EDA
   │
   ▼
Feature Engineering
   │
   ▼
Preprocessing
   │
   ▼
Train-Test Split
   │
   ▼
Linear Regression
   │
   ▼
Model Evaluation
   │
   ▼
Model Deployment
```

---

# 📈 Evaluation Metrics

The model is evaluated using:

- MAE
- MSE
- RMSE
- R² Score

---

# 📁 Project Structure

```text
Manufacturing_Output_Prediction/
│
├── manufacturing_equipment_output_prediction.ipynb
├── manufacturing_dataset_1000_samples.csv
├── linear_regression.pkl
├── main.py
├── requirements.txt
├── Dockerfile
├── README.md
└── screenshots/
```

---

# ▶ Running the Project

## Clone Repository

```bash
git clone https://github.com/yourusername/Manufacturing-Equipment-Output-Prediction.git

cd Manufacturing-Equipment-Output-Prediction
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run FastAPI

```bash
uvicorn main:app --reload
```

Visit

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker

Build Image

```bash
docker build -t manufacturing-api .
```

Run Container

```bash
docker run -p 8000:8000 manufacturing-api
```

---

# 📷 API Documentation

FastAPI automatically generates Swagger documentation.

Open:

```
http://127.0.0.1:8000/docs
```

---

# 📌 Future Improvements

- Hyperparameter Tuning
- Multiple Regression Models
- Model Monitoring
- Cloud Deployment
- Streamlit Dashboard
- CI/CD Pipeline

---

# 👩‍💻 Author

**Shravani Kavle**

Artificial Intelligence & Data Science Engineering Student

---

⭐ If you found this project useful, consider giving it a star.
