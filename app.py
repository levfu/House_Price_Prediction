import streamlit as st
import pandas as pd
import joblib

# 1. Page Configuration
st.set_page_config(page_title = "House Price Predictor", layout = "centered")

# 2. Load Model and Baseline Data
@st.cache_resource
def load_model():
    return joblib.load('house_price_model.pkl')

@st.cache_data
def load_baseline():
    # Load data to get column names and create a 'Baseline House'
    df = pd.read_csv('data/train.csv')
    X = df.drop(columns = ['Id', 'SalePrice'])
    # Use the first house in the dataset as our default template
    baseline = X.iloc[0:1].copy()
    return baseline

model = load_model()
baseline_df = load_baseline()

# 3. Web App Interface
st.title('Real Estate AI: Price Predictor')
st.markdown("Adjust the key features below to get an instant AI valuation for your property.")

st.divider()

# Create 2 columns for better UI layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Core Features")
    overall_qual = st.slider('Overall Material & Finish Quality (1-10)', 1, 10, int(baseline_df['OverallQual'].values[0]))
    gr_liv_area = st.number_input('Above Ground Living Area (sqft)', min_value = 500, max_value = 5000, value = int(baseline_df['GrLivArea'].values[0]), step = 50)
    total_bsmt_sf = st.number_input('Total Basement Area (sqft)', min_value = 0, max_value = 3000, value = int(baseline_df['TotalBsmtSF'].values[0]), step = 50)

with col2:
    st.subheader("📍 Details & Location")
    year_built = st.slider('Original Construction Date', 1870, 2020, int(baseline_df['YearBuilt'].values[0]))
    garage_cars = st.slider('Garage Capacity (Cars)', 0, 5, int(baseline_df['GarageCars'].values[0]))
    neighborhood = st.selectbox('Neighborhood', ['CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel', 'Somerst', 'NWAmes', 'OldTown', 'BrkSide', 'Sawyer', 'NridgHt', 'NAmes', 'SawyerW', 'IDOTRR', 'MeadowV', 'Edwards', 'Timber', 'Gilbert', 'StoneBr', 'ClearCr', 'NPkVill', 'Blmngtn', 'BrDale', 'SWISU'])

st.divider()

# 4. Predict Button
if st.button('🔮 Predict Price', use_container_width = True):
    # Overwrite baseline template with user inputs
    user_input = baseline_df.copy()
    user_input['OverallQual'] = overall_qual
    user_input['GrLivArea'] = gr_liv_area
    user_input['TotalBsmtSF'] = total_bsmt_sf
    user_input['YearBuilt'] = year_built
    user_input['GarageCars'] = garage_cars
    user_input['Neighborhood'] = neighborhood

    # AI Prediction
    prediction = model.predict(user_input)[0]
    
    # Display Result
    st.success(f"### Estimated Market Value: **${prediction:,.0f}**")
    st.balloons()