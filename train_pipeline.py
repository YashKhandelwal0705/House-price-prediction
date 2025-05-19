import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv("data.csv")

# Drop unnecessary columns
df.drop(columns=["date", "street", "city", "statezip", "country", "price"], inplace=False)

# Select features and target
X = df[[
    'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
    'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement',
    'yr_built', 'yr_renovated'
]]
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train pipeline
pipeline.fit(X_train, y_train)

# Save pipeline
joblib.dump(pipeline, "best_model.pkl")

print("✅ Pipeline trained and saved as best_model.pkl")
