import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('best_model.pkl')

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏠 House Price Prediction App")

# Input fields
bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=20, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=10, step=1)
sqft_living = st.number_input("Living Area (in sqft)", min_value=100)
sqft_lot = st.number_input("Lot Size (in sqft)", min_value=100)
floors = st.number_input("Number of Floors", min_value=1.0, max_value=4.0, step=0.5)
waterfront = st.selectbox("Waterfront View?", ["No", "Yes"])
view = st.slider("View Rating (0-4)", 0, 4, 0)
condition = st.slider("Condition (1-5)", 1, 5, 3)
sqft_above = st.number_input("Sqft Above Ground", min_value=100)
sqft_basement = st.number_input("Sqft Basement", min_value=0)
yr_built = st.number_input("Year Built", min_value=1800, max_value=2025, step=1)
yr_renovated = st.number_input("Year Renovated (0 if never)", min_value=0, max_value=2025, step=1)

# Encode categorical features
waterfront = 1 if waterfront == "Yes" else 0

# Feature array
features = np.array([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                      waterfront, view, condition, sqft_above, sqft_basement,
                      yr_built, yr_renovated]])

# Prediction
if st.button("Predict Price"):
    price = model.predict(features)[0]
    st.success(f"Estimated House Price: ₹ {price:,.2f}")