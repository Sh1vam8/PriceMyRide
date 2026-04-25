# 🚗 PriceMyRide – AutoMarket Intelligence Dashboard

An interactive **machine learning-powered car price prediction and market intelligence dashboard** built with Streamlit.
This project combines **data analytics, feature engineering, and predictive modeling** to simulate a real-world automotive pricing platform.

---

## 📌 Overview

PriceMyRide is designed as a **decision-support tool** for buyers, sellers, and analysts in the used car market.
It enables users to:

* Predict car prices using ML
* Analyze market trends
* Evaluate whether a car is overpriced or a good deal

---

## 🔥 Features

### 💰 AI Price Prediction

* Predicts car price based on:

  * Fuel type
  * Transmission
  * Ownership
  * Kilometers driven

---

### 📊 Market Intelligence Dashboard

Includes key KPIs:

* Average Market Price
* Predicted Price Average
* Model Error (Accuracy Insight)
* Overpriced vs Underpriced %

---

### 🧠 Deal Evaluation Engine

Compare your expected price with model prediction:

* 🔥 Good Deal (Below Market)
* ⚖️ Fair Price
* 🚨 Overpriced

---

### 🎯 Smart Filters

Dynamic filtering using sidebar:

* Brand (engineered from data)
* Model
* Fuel Type
* Transmission
* Ownership
* KMS Driven
* Price Range (Crores → internally converted to Lakhs)

---

### 📈 Visual Analytics

* Scatter Plot → Price vs KMS
* Histogram → Price Distribution

---

### 📄 Data Explorer

* View filtered dataset
* Download as CSV

---

## 🧠 Tech Stack

| Layer         | Technology   |
| ------------- | ------------ |
| Frontend      | Streamlit    |
| Backend       | Python       |
| Data Handling | Pandas       |
| Visualization | Matplotlib   |
| ML Model      | Scikit-learn |

---

## ⚙️ Data Engineering Highlights

* Cleaned and standardized dataset columns
* Engineered `brand` and `model` from raw `car_name`
* Implemented categorical encoding for ML compatibility
* Maintained unit consistency (Crores ↔ Lakhs)

---

## 📊 Project Structure

```
PriceMyRide/
│
├── app.py
├── final_model.pkl
├── Car Dataset Processed.csv
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

### 1. Clone Repository

```
git clone https://github.com/your-username/PriceMyRide.git
cd PriceMyRide
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Application

```
streamlit run app.py
```

---

## 💡 Use Case

This dashboard simulates a **real-world automotive marketplace tool**:

* Buyers → Identify best deals
* Sellers → Price competitively
* Analysts → Study pricing trends

---

## 📬 Contact

For collaboration or feedback:

* GitHub:  Sh1vam8  

---

## ⭐ If You Found This Useful

Give this project a ⭐ on GitHub to support the work!
