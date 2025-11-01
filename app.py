import streamlit as st
import seaborn as sns
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import gdown
import os
import requests


# URL model di GitHub (gunakan link RAW)
# ✅ Pastikan URL RAW dari GitHub
MODEL_URL = "https://github.com/agna2103/pohon_rumah/raw/main/handwriting_model.keras"
MODEL_PATH = "handwriting_model.keras"

# 🔹 Unduh model hanya jika belum ada
if not os.path.exists(MODEL_PATH):
    print("Mengunduh model dari GitHub...")
    r = requests.get(MODEL_URL)
    if r.status_code == 200:
        with open(MODEL_PATH, "wb") as f:
            f.write(r.content)
        print("Model berhasil diunduh.")
    else:
        raise Exception(f"Gagal mengunduh model. Status: {r.status_code}")

# 🔹 Coba load model dengan error handling
try:
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    print("✅ Model berhasil dimuat.")
except Exception as e:
    print("❌ Gagal memuat model:", str(e))
    # --- Coba mode fallback ---
    print("Mencoba memuat ulang model dengan custom input shape...")
    model = tf.keras.models.load_model(MODEL_PATH, compile=False, safe_mode=False)



sns.set(style='dark')
st.set_page_config(page_title= "AI Dalam Psikologi",page_icon="𝚿",layout= "wide")
st.header("AI Dalam Psikologi 𝚿")
with st.container():
    st.title("🖍️ Tempat Menggambar")
    st.write("Gunakan area di bawah ini untuk menggambar pohon rumah dan orang")

    left_column, right_column = st.columns(2)
    with right_column:
        # Pilihan warna dan ukuran kuas
        stroke_color = st.color_picker("Pilih warna kuas:", "#000000")
        stroke_width = st.slider("Ukuran kuas:", 1, 25, 5)
    with left_column:    
        # Tempat menggambar (canvas)
        canvas_result = st_canvas(
            fill_color="rgba(255, 255, 255, 1)",  # warna latar belakang
            stroke_width=stroke_width,
            stroke_color=stroke_color,
            background_color="#FFFFFF",
            height=400,
            width=600,
            drawing_mode="freedraw",  
            key="canvas",
        )
    left_column, right_column = st.columns(2)
    with left_column:
        # Jika pengguna sudah menggambar sesuatu
        if canvas_result.image_data is not None:
            st.write("Hasil Gambar")
            st.image(canvas_result.image_data)
    with right_column:
        # Tombol untuk mendeteksi Gambar
        if st.button("Deteksi Gambar"):
            st.write("Sedang Mendeteksi")
    
    st.write("---")

with st.container():
    st.write("---")
    st.caption("agna aldhaka-contoh penggunaan cnn untuk deteksi gambar")
