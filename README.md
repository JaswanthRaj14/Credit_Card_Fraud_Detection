# 💳 Credit Card Fraud Detection

## 📖 Project Overview

Credit card fraud is one of the biggest challenges faced by financial institutions due to the increasing number of online transactions. Detecting fraudulent transactions accurately is essential to minimize financial losses while avoiding false alarms for genuine customers.

This project implements a **Machine Learning-based Credit Card Fraud Detection System** that classifies transactions as **Legitimate** or **Fraudulent**. The model is trained using historical transaction data and deployed as an interactive **Streamlit** web application where users can upload transaction data and receive fraud predictions instantly.

---

## 🎯 Objectives

* Build a reliable machine learning model for fraud detection.
* Handle real-world transaction data through preprocessing.
* Predict whether a transaction is fraudulent or legitimate.
* Provide an easy-to-use web interface for batch prediction.
* Demonstrate an end-to-end Machine Learning workflow.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Machine Learning:** Scikit-learn
* **Data Processing:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Model Serialization:** Joblib
* **Web Framework:** Streamlit

---

## 📂 Project Structure

```text
Credit-Card-Fraud-Detection/
│
├── Credit_Card_Fraud_Detection.ipynb   # Model training & evaluation
├── app.py                              # Streamlit application
├── credit_card_model                   # Trained ML model
├── requirements.txt                    # Required dependencies
├── README.md                           # Project documentation
```

---

## 🔄 Machine Learning Workflow

1. Load the credit card transaction dataset.
2. Perform data preprocessing and cleaning.
3. Prepare the dataset for model training.
4. Train a **Random Forest Classifier**.
5. Evaluate the model on unseen data.
6. Save the trained model using **Joblib**.
7. Deploy the model using **Streamlit**.
8. Upload new transaction data and generate fraud predictions.

---

## ✨ Features

* Data preprocessing before prediction.
* Fraud detection using a trained Random Forest model.
* Batch prediction through CSV file upload.
* Automatically labels transactions as:

  * ✅ Legitimate Transaction
  * ⚠️ Fraudulent Transaction
* Displays prediction summary, including:

  * Total Transactions
  * Fraudulent Transactions
  * Legitimate Transactions

---

## 📊 Dataset

This project uses the **Credit Card Fraud Detection Dataset** available on Kaggle.

**Dataset Link:**

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

> **Note:** The dataset is not included in this repository because of its size and licensing considerations.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/JaswanthRaj14/Credit-Card-Fraud-Detection.git
```

Move into the project directory:

```bash
cd Credit-Card-Fraud-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📈 Model

**Algorithm Used**

* Random Forest Classifier

The trained model predicts whether a transaction is fraudulent based on transaction features.

---

## 📸 Application Workflow

1. Launch the Streamlit application.
2. Upload a CSV file containing transaction records.
3. The trained model processes the data.
4. View individual predictions.
5. Review the summary of fraudulent and legitimate transactions.

---

## 🔮 Future Improvements

* Compare multiple machine learning algorithms (XGBoost, LightGBM, CatBoost).
* Build a deep learning model for fraud detection.
* Deploy the application on Streamlit Cloud or Render.
* Add interactive visualizations and analytics dashboard.
* Support real-time transaction prediction through APIs.

---

## 📚 Learning Outcomes

This project demonstrates:

* Data preprocessing
* Machine Learning model development
* Model evaluation
* Model serialization with Joblib
* Streamlit application development
* End-to-end ML deployment

---

## 👨‍💻 Author

**Ramjaaly Jaswanth Raj**

Aspiring **Data Scientist | Data Analyst | Machine Learning Enthusiast**

If you found this project useful, consider giving it a ⭐ on GitHub.
