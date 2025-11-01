import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
sns.set(style='dark')

#membuka dataframe
url_year = "https://github.com/agna2103/l_analisis_data/blob/main/dashboard/years.csv?raw=true"
url_month = "https://github.com/agna2103/l_analisis_data/blob/main/dashboard/month.csv?raw=true"
year_df = pd.read_csv(url_year, index_col=0)
month_df = pd.read_csv(url_month, index_col=0)

st.set_page_config(page_title= "AIR QUALITY INDEX SUBMISSION",page_icon="🌍",layout= "wide")

with st.container():
    st.subheader("Air Quality Index 🌍")
    st.title("Apa itu Air Quality Index ?")
    st.write("air quality index merupakan parameter yang dapat digunakan untuk menilai seberapa buruk tingkat polusi udara. air quality index menggunakan skala 1-500, semakin tinggi nilai aqi maka semakin buruk pollusi udara yang terjadi.")
    st.write("[learn more >](https://www.airnow.gov/aqi/aqi-basics/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.subheader("Indeks kualitas udara rata-rata selama tahun 2013-2017")
        st.write("###")
        st.write(" dari grafik yang dihasilkan dapat diketahui bahwa nilai kualitas udara bervariasi sepanjang tahun dengan nilai terburuk terjadi pada tahun 2014 dengan kategori unhealthy. nilai tersebut kemudian menurun ditahun tahun setelahnya. dapat diketahui pula bahwa stasiun Aothizhongsin memiliki kualitas udara yang paling buruk dan stasiun kota changpin memiliki kualitas udara yang paling baik")
    with left_column:
        fig, ax = plt.subplots(figsize=(15,8))
        year_df['year'] = range(2013, 2013 + len(year_df))
        
        sns.lineplot(x= np.asarray(year_df['year']).astype(str),y= year_df['AQI_x'], color='blue', label='Kota AotiZhongxin')
        sns.lineplot(x= np.asarray(year_df['year']).astype(str),y= year_df['AQI_y'], color='green', label='Kota Chanping')
        sns.lineplot(x= np.asarray(year_df['year']).astype(str),y= year_df['AQI'], color='red', label='Kota Dongsi')
        ax.set_xlabel('Tahun',size=15)
        ax.set_ylabel('Air Quality Index',size=15)
        ax.set_title("Indeks kualitas udara selama tahun 2013-2017", size=20)
        ax.legend()
        st.pyplot(fig)
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.subheader("Indeks kualitas udara berdasarkan bulan")
        st.write("###")
        st.write("dari grafik yang dihasilkan  dapat diisimpulkan bahwa tingkat polusi udara tertinggi terjadi pada bulan 6-7 (musim panas) dan nilai polusi terendah terjadi pada bulan 9 (musim gugur)")
    with left_column:
        fig, ax = plt.subplots(figsize=(15,8))
        month_df['month'] = range(1, 1 + len(month_df))
        
        sns.lineplot(x= np.asarray(month_df['month']).astype(str), y= month_df['AQI_x'], color='blue', label='Kota AotiZhongxin')
        sns.lineplot(x= np.asarray(month_df['month']).astype(str), y= month_df['AQI_y'], color='green', label='Kota Chanping')
        sns.lineplot(x= np.asarray(month_df['month']).astype(str), y= month_df['AQI'], color='red', label='Kota Dongsi')
        ax.set_xlabel('bulan',size=15)
        ax.set_ylabel('Air Quality Index',size=15)
        ax.set_title("Indeks kualitas udara berdasarkan bulan", size=20)
        ax.legend()
        st.pyplot(fig)
with st.container():
    st.write("---")
    st.caption("agna aldhaka-dicoding submission")
