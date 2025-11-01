import streamlit as st
import seaborn as sns
sns.set(style='dark')
st.set_page_config(page_title= "AI Dalam Psikologi",page_icon="𝚿",layout= "wide")
st.header("AI Dalam Psikologi 𝚿")
with st.container():
    st.subheader("Air Quality Index 🌍")
    st.title("Apa itu Air Quality Index ?")
    st.write("air quality index merupakan parameter yang dapat digunakan untuk menilai seberapa buruk tingkat polusi udara. air quality index menggunakan skala 1-500, semakin tinggi nilai aqi maka semakin buruk pollusi udara yang terjadi.")
    st.write("[learn more >](https://www.airnow.gov/aqi/aqi-basics/)")
with st.container():
    st.write("---")
    st.caption("agna aldhaka-contoh penggunaan cnn untuk deteksi gambar")
