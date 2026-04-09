# Real Estate AI: House Price Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](THAY_LINK_WEB_STREAMLIT_CỦA_BẠN_VÀO_ĐÂY)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange.svg)](https://scikit-learn.org/)

## Overview
This project is an end-to-end Machine Learning web application designed to predict the market value of residential properties in Ames, Iowa. By leveraging advanced regression techniques and an automated data preprocessing pipeline, the AI model provides instant and accurate price estimates based on key property features.

## Key Features
* **Automated Data Pipeline:** Built a robust `scikit-learn` Pipeline utilizing `SimpleImputer`, `StandardScaler`, and `OneHotEncoder` to automatically handle missing values and categorical data while strictly preventing **Data Leakage**.
* **Outlier Handling:** Conducted Exploratory Data Analysis (EDA) to identify and remove critical outliers, significantly improving the model's boundary decision.
* **Hyperparameter Tuning & Evaluation:** Trained and compared multiple algorithms including Linear Regression, Ridge (L2), Lasso (L1), and Random Forest (tuned via `GridSearchCV`).
* **Feature Selection via Lasso:** The champion model, **Lasso Regression**, achieved an **$R^2$ Score of 90.40%** by inherently performing feature selection (shrinking irrelevant feature weights to zero) in a highly dimensional dataset.
* **Interactive UI:** Deployed an intuitive and responsive web interface using **Streamlit**.

## Tech Stack
* **Language:** Python
* **Data Processing & EDA:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn, Joblib
* **Web Framework & Deployment:** Streamlit, Streamlit Community Cloud

## Project Structure
```text
House_Price_Prediction/
│
├── data/
│   ├── train.csv                # Raw Ames Housing dataset
│   └── data_description.txt     # Data dictionary
│
├── notebooks/
│   ├── 01_EDA.ipynb             # Exploratory Data Analysis & Visualizations
│   └── 02_Model_Training.ipynb  # Pipeline building, Model training, & Tuning
│
├── app.py                       # Streamlit web application script
├── house_price_model.pkl        # Exported champion model (Lasso)
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## How to Run Locally
1. **Clone the repository:**
```bash
   git clone [https://github.com/](https://github.com/)[YOUR_GITHUB_USERNAME]/House_Price_Prediction.git
   cd House_Price_Prediction
