import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="PriceMyRide Dashboard", layout="wide")
st.title("🚗 PriceMyRide Intelligence Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("Car Dataset Processed.csv")
df.columns = df.columns.str.strip().str.lower()

# Feature Engineering
df["Year"] = df["car_name"].apply(lambda x: x.split()[0])
df["model"] = df["car_name"].apply(lambda x: " ".join(x.split()[1:]))

# -----------------------------
# LOAD MODEL
# -----------------------------
model = pickle.load(open("final_model.pkl", "rb"))

# -----------------------------
# ENCODINGS (DEFINE ONCE)
# -----------------------------
k1 = {'Comprehensive':0,'Third Party insurance':1,'Zero Dep':2,'Not Available':3,'Third Party':1}
k2 = {'Petrol':1,'Diesel':2,'CNG':3}
k3 = {'First Owner':1,'Second Owner':2,'Third Owner':3,'Fifth Owner':5}
k4 = {'Manual':7,'Automatic':8}

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("🔍 Filters")

Year = st.sidebar.selectbox("Year", sorted(df["Year"].unique()))
model_name = st.sidebar.selectbox("Model", df[df["Year"] == Year]["model"].unique())

fuel_type = st.sidebar.selectbox("Fuel Type", df["fuel_type"].unique())
transmission = st.sidebar.selectbox("Transmission", df["transmission"].unique())
ownership = st.sidebar.selectbox("Ownership", df["ownership"].unique())

kms_driven = st.sidebar.slider("KMS Driven", 0, 200000, 30000)

# Price Range (Crores)
price_range = st.sidebar.slider("💰 Price Range (Cr)", 0.0, 2.0, (0.0, 0.5))
min_price, max_price = price_range[0]*100, price_range[1]*100

st.sidebar.write(f"Selected Range: ₹ {price_range[0]:.2f}Cr - ₹ {price_range[1]:.2f}Cr")

# -----------------------------
# FILTER DATA
# -----------------------------
filtered_df = df[
    (df["Year"] == Year) &
    (df["model"] == model_name) &
    (df["price(in lakhs)"] >= min_price) &
    (df["price(in lakhs)"] <= max_price)
]

# -----------------------------
# MODEL PREDICTIONS (BATCH)
# -----------------------------
temp_df = None

if not filtered_df.empty:
    try:
        temp_df = filtered_df.copy()

        temp_df["insurance_validity"] = temp_df["insurance_validity"].map(k1)
        temp_df["fuel_type"] = temp_df["fuel_type"].map(k2)
        temp_df["ownership"] = temp_df["ownership"].map(k3)
        temp_df["transmission"] = temp_df["transmission"].map(k4)

        temp_df = temp_df.dropna()

        features = ["insurance_validity","fuel_type","kms_driven","ownership","transmission"]
        temp_df["predicted_price"] = model.predict(temp_df[features])

    except:
        temp_df = None

# -----------------------------
# KPI METRICS
# -----------------------------
st.subheader("📊 Key Market + Model Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

if not filtered_df.empty:
    avg_price = filtered_df["price(in lakhs)"].mean()
    col1.metric("Avg Price", f"₹ {avg_price:.2f} L")

    if temp_df is not None and not temp_df.empty:
        predicted_avg = temp_df["predicted_price"].mean()
        error = temp_df["price(in lakhs)"] - temp_df["predicted_price"]

        col2.metric("Predicted Avg", f"₹ {predicted_avg:.2f} L")
        col3.metric("Avg Error", f"₹ {error.mean():.2f} L")
        col4.metric("Overpriced %", f"{(error < 0).mean()*100:.1f}%")
        col5.metric("Underpriced %", f"{(error > 0).mean()*100:.1f}%")
else:
    st.warning("No data available")

# -----------------------------
# PREDICTION + DEAL EVALUATION
# -----------------------------
st.subheader("💰 Price Prediction & Deal Analysis")

user_price = st.slider("Your Price (Lakhs)", 0.0, 200.0, 5.0)

test = [[
    k1.get('Comprehensive', 0),
    k2[fuel_type],
    kms_driven,
    k3[ownership],
    k4[transmission]
]]

predicted = model.predict(test)[0]

colA, colB = st.columns(2)

with colA:
    st.metric("Predicted Price", f"₹ {predicted:.2f} L")

with colB:
    diff = user_price - predicted
    st.metric("Your vs Market", f"₹ {diff:.2f} L")

# Deal Evaluation
if diff < 0:
    st.success("🔥 Good Deal")
elif diff < 1:
    st.info("⚖️ Fair Price")
else:
    st.error("🚨 Overpriced")

# -----------------------------
# VISUALIZATION
# -----------------------------
st.subheader("📈 Market Insights")

if not filtered_df.empty:
    fig, ax = plt.subplots()
    ax.scatter(filtered_df["kms_driven"], filtered_df["price(in lakhs)"])
    ax.set_xlabel("KMS")
    ax.set_ylabel("Price (L)")
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.hist(filtered_df["price(in lakhs)"], bins=20)
    st.pyplot(fig2)

# -----------------------------
# DATA + DOWNLOAD
# -----------------------------
st.subheader("📄 Data Explorer")
st.dataframe(filtered_df.head(50))

st.download_button(
    "📥 Download Data",
    filtered_df.to_csv(index=False),
    "filtered_data.csv"
)