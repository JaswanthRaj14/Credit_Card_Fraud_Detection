import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("credit_card_model")

st.title("💳 Credit Card Fraud Detection")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file with transaction data", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Drop columns that shouldn't go into model
    if "Class" in data.columns:
        data = data.drop(columns=["Class"])
    if "Time" in data.columns:
        data = data.drop(columns=["Time"])

    # Make predictions
    predictions = model.predict(data)

    # Add results to dataframe
    result_df = pd.DataFrame(predictions, columns=["Prediction"])
    result_df["Prediction"] = result_df["Prediction"].map({0: "✅ Not Fraud", 1: "⚠️ Fraud"})

    st.subheader("🔍 Prediction Results")
    st.write(result_df)

    # Show summary
    fraud_count = (predictions == 1).sum()
    total = len(predictions)

    st.subheader("📊 Summary")
    st.write(f"Total Transactions: {total}")
    st.write(f"Fraudulent Transactions: {fraud_count}")
    st.write(f"Legitimate Transactions: {total - fraud_count}")
