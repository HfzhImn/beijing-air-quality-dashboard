import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set page config
st.set_page_config(page_title="Beijing Air Quality Dashboard", layout="wide")

# Load data bersih
def load_data():
    df = pd.read_csv("dashboard/main_data.csv")
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

all_df = load_data()

# --- SIDEBAR ---
with st.sidebar:
    st.title("Filter Data")
    
    # Filter Rentang Waktu
    min_date = all_df["datetime"].min()
    max_date = all_df["datetime"].max()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    # Filter Stasiun
    stasiun_options = all_df["station"].unique()
    selected_stations = st.multiselect(
        "Pilih Stasiun Pemantauan",
        options=stasiun_options,
        default=stasiun_options
    )

# Filter Data Berdasarkan Sidebar
main_df = all_df[(all_df["datetime"] >= pd.to_datetime(start_date)) & 
                 (all_df["datetime"] <= pd.to_datetime(end_date)) &
                 (all_df["station"].isin(selected_stations))]

# --- MAIN PAGE ---
st.title("📊 Beijing Air Quality Dashboard")
st.markdown("Dashboard ini menampilkan analisis kualitas udara (PM2.5) di berbagai stasiun pemantauan di Beijing.")

# Row 1: Metrics
col1, col2, col3 = st.columns(3)
with col1:
    avg_pm25 = round(main_df["PM2.5"].mean(), 2)
    st.metric("Rata-rata PM2.5", value=avg_pm25)
with col2:
    max_pm25 = main_df["PM2.5"].max()
    st.metric("Polusi Tertinggi", value=max_pm25)
with col3:
    st.metric("Total Data Teranalisis", value=len(main_df))

st.divider()

# Row 2: Tren Bulanan & Perbandingan Stasiun
c1, c2 = st.columns(2)

with c1:
    st.subheader("Tren Bulanan PM2.5")
    monthly_df = main_df.resample(rule='ME', on='datetime').agg({"PM2.5": "mean"}).reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(monthly_df["datetime"], monthly_df["PM2.5"], marker='o', linewidth=2, color="#b03a2e")
    ax.set_ylabel("Konsentrasi PM2.5")
    st.pyplot(fig)

with c2:
    st.subheader("Rata-rata PM2.5 per Stasiun")
    station_df = main_df.groupby("station")["PM2.5"].mean().sort_values(ascending=False).reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=station_df, x="PM2.5", y="station", palette="Reds_r", ax=ax)
    st.pyplot(fig)

# Row 3: Analisis Lanjutan (Korelasi & AQI)
st.divider()
st.subheader("Korelasi Faktor Cuaca (Kecepatan Angin) terhadap PM2.5")

fig, ax = plt.subplots(figsize=(12, 6))
sns.scatterplot(
    data=main_df.sample(2000), # Gunakan sample agar dashboard tidak berat saat loading
    x="WSPM", 
    y="PM2.5", 
    hue="station", 
    alpha=0.5,
    ax=ax
)
st.pyplot(fig)

st.info("""
**Insight:** Terlihat pola korelasi negatif di mana kecepatan angin yang lebih tinggi cenderung 
membantu menurunkan konsentrasi polutan PM2.5 di udara.
""")

st.caption("Copyright (c) Hafizh Iman Wicaksono 2026")