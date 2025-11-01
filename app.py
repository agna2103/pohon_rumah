import streamlit as st
import seaborn as sns
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
import numpy as np
import gdown
import os
import requests

def build_model():
    # Bangun model dasar (pretrained)
    base_model = MobileNetV2(
        input_shape=(160, 160, 3),
        include_top=False,
        weights='imagenet'
    )
    
    # Bekukan semua layer sementara
    base_model.trainable = False

    # Tambahkan lapisan kustom di atas base model
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.4),
        layers.Dense(3, activation='softmax')  # 3 kelas: house, person, tree
    ])

    # Kompilasi model
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    # Fine-tuning parsial: aktifkan kembali sebagian layer setelah compile
    base_model.trainable = True
    for layer in base_model.layers[:100]:
        layer.trainable = False

    return model
st.info(print"✅ Model berhasil dibangun dan bobot dimuat")
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
