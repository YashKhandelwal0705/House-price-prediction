# House-price-prediction
Project Overview
In today’s fast-evolving technological landscape, machine learning is a key tool to solve real-world problems. Predicting house prices is one such impactful application that benefits homeowners, buyers, and real estate professionals by providing accurate property valuations.

This project implements multiple machine learning algorithms — Logistic Regression, Decision Trees, and Random Forests — to forecast house prices using features like bedrooms, bathrooms, living space, lot size, floors, and more.

The solution is encapsulated in a complete Scikit-learn pipeline that integrates preprocessing (scaling) and model training, ensuring robust and reproducible predictions.

A user-friendly Streamlit app offers an interactive front-end where users can input house details and get instant price predictions, making this tool accessible even without programming knowledge.

Features
Multiple ML algorithms for price prediction

End-to-end Scikit-learn pipeline including preprocessing

Hyperparameter tuning for optimized accuracy

Interactive Streamlit interface for easy use

Support for a wide range of housing features

Dataset
The model is trained on a comprehensive housing dataset containing features such as:

Date of sale

Price

Bedrooms

Bathrooms

Square footage (living and lot)

Floors

Waterfront presence

View rating

Condition

Year built and renovated

Location details (street, city, state, zip, country)

Installation
Clone the repo:

bash
Copy
Edit
git clone https://github.com/YashKhandelwal0705/House-price-prediction.git
cd House-price-prediction
(Recommended) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Train the Model Pipeline
Make sure the dataset file (e.g., kc_house_data.csv) is in the project directory.

Run the training script:

bash
Copy
Edit
python train_pipeline.py
This will train the model pipeline and save it as best_model.pkl.

Run the Streamlit App
Start the interactive app:

bash
Copy
Edit
streamlit run app.py
Open the URL provided by Streamlit in your browser. Input house features and get price predictions instantly.

Deployment
The app can be deployed free and easily on Streamlit Community Cloud:

Push your repo to GitHub.

Sign in to Streamlit Cloud.

Connect your GitHub repo and select app.py to deploy.

Make sure your requirements.txt lists all dependencies for automatic setup.

Contributing
Contributions are welcome! Feel free to:

Improve model accuracy

Add new features or visualizations

Enhance the app UI

Optimize pipeline performance

Please open issues or submit pull requests.

License
This project is open source and available under the MIT License.







