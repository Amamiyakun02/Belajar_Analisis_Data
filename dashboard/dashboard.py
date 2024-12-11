
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

st.set_page_config(page_title="Analisis Kualitas Udara di Wanshouxigong oleh M. Maireza")
data = pd.read_csv('./data/PRSA_Data_Wanshouxigong_20130301-20170228.csv')

st.title('Air Quality Analysis Dashboard: Wanshouxigong Station')

st.write('Dashboard interaktif ini memberikan cara eksplorasi data kualitas udara, dengan fokus khusus pada tingkat PM2.5 dan hubungannya dengan berbagai kondisi cuaca.')

# About me
st.markdown("""
### About Me
- **Name**: M. Maireza
- **Email Address**: mmaireza@mhs.politala.ac.id
- **Dicoding ID**: [maireza](https://www.dicoding.com/users/maireza/academies)

### Gambaran Proyek
Dasbor ini menyajikan analisis data kualitas udara, dengan perhatian khusus pada tingkat PM2.5 dari stasiun Wanshouxigong. Proyek ini bertujuan untuk mengungkap tren, variasi musiman, dan dampak berbagai kondisi cuaca terhadap kualitas udara. Wawasan dari analisis ini dapat bermanfaat bagi studi lingkungan dan pemantauan kesehatan masyarakat.
""")

st.sidebar.header('Fitur Input User')

selected_year = st.sidebar.selectbox('Pilih Tahun', list(data['year'].unique()))
selected_month = st.sidebar.selectbox('Pilih Bulan', list(data['month'].unique()))

data_filtered = data[(data['year'] == selected_year) & (data['month'] == selected_month)].copy()

# Displaying data statistics
st.subheader('Overview Data untuk Periode Terpilih')
st.write(data_filtered.describe())

st.subheader('Tingkat PM2.5 Harian')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM2.5'])
plt.xlabel('Day of the Month')
plt.ylabel('PM2.5 Concentration')
st.pyplot(fig)

st.subheader('Peta Panas Korelasi Indikator Kualitas Udara')
corr = data_filtered[['PM2.5', 'NO2', 'SO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
plt.title('Correlation Heatmap')
st.pyplot(fig)

# Seasonal Trend Analysis
st.subheader('Analisis Tren Musiman')
seasonal_trends = data.groupby('month')['PM2.5'].mean()
fig, ax = plt.subplots()
seasonal_trends.plot(kind='bar', color='skyblue', ax=ax)
plt.title('Average Monthly PM2.5 Levels')
plt.xlabel('Month')
plt.ylabel('Average PM2.5')
st.pyplot(fig)

# Daily PM2.5 Levels
st.subheader('Daily PM2.5 Levels')
fig, ax = plt.subplots()
ax.plot(data_filtered['day'], data_filtered['PM2.5'])
plt.xlabel('Day of the Month')
plt.ylabel('PM2.5 Concentration')
st.pyplot(fig)

# Pollutant Distribution
st.subheader('Distribusi Polutan')
selected_pollutant = st.selectbox('Select Pollutant', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO'])
fig, ax = plt.subplots()
sns.boxplot(x='month', y=selected_pollutant, data=data[data['year'] == selected_year], ax=ax)
st.pyplot(fig)

st.subheader('Dekomposisi Time Series PM2.5')
try:
    data_filtered['PM2.5'].ffill(inplace=True)
    decomposed = seasonal_decompose(data_filtered['PM2.5'], model='additive', period=24) # Adjust period as necessary
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
    decomposed.trend.plot(ax=ax1, title='Trend')
    decomposed.seasonal.plot(ax=ax2, title='Seasonality')
    decomposed.resid.plot(ax=ax3, title='Residuals')
    plt.tight_layout()
    st.pyplot(fig)
except ValueError as e:
    st.error("Unable to perform time series decomposition: " + str(e))


st.subheader('Rata-Rata Per Jam PM2.5')
try:
    # Ensure correct data types and handle missing values
    data['hour'] = data['hour'].astype(int)
    data['PM2.5'] = pd.to_numeric(data['PM2.5'], errors='coerce')
    data['PM2.5'].ffill(inplace=True)

    # Calculate hourly averages
    hourly_avg = data.groupby('hour')['PM2.5'].mean()

    # Plotting
    fig, ax = plt.subplots()
    sns.heatmap([hourly_avg.values], ax=ax, cmap='coolwarm')
    plt.title('Hourly Averages of PM2.5')
    st.pyplot(fig)
except Exception as e:
    st.error(f"Error in plotting hourly averages: {e}")

st.subheader('Analisis Arah Angin')
wind_data = data_filtered.groupby('wd')['PM2.5'].mean()
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
theta = np.linspace(0, 2 * np.pi, len(wind_data))
bars = ax.bar(theta, wind_data.values, align='center', alpha=0.5)
plt.title('PM2.5 Levels by Wind Direction')
st.pyplot(fig)

st.subheader('Curah Hujan vs Tingkat PM2.5')
fig, ax = plt.subplots()
sns.scatterplot(x='RAIN', y='PM2.5', data=data_filtered, ax=ax)
plt.title('Rainfall vs. PM2.5 Levels')
st.pyplot(fig)

st.subheader('Peta Panas Korelasi Interaktif')
selected_columns = st.multiselect('Select Columns for Correlation', data.columns, default=['PM2.5', 'NO2', 'TEMP', 'PRES', 'DEWP'])
corr = data[selected_columns].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, ax=ax)
st.pyplot(fig)

st.subheader('Kesimpulan')

st.write("""
- Dasbor ini memberikan analisis mendalam dan interaktif tentang data kualitas udara.
- Berbagai visualisasi menawarkan wawasan tentang tingkat PM2.5, distribusinya, dan faktor-faktor yang memengaruhinya.
- Tren musiman dan dampak kondisi cuaca serta polutan terhadap kualitas udara digambarkan dengan jelas.
- Pengguna dapat mengeksplorasi data secara dinamis untuk memperoleh pemahaman yang lebih mendalam tentang tren kualitas udara.
""")
