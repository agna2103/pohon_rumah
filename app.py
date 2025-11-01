import streamlit as st
import seaborn as sns
sns.set(style='dark')
st.set_page_config(page_title= "AI Dalam Psikologi",page_icon="𝚿",layout= "wide")
st.header("AI Dalam Psikologi 𝚿")
with st.container():
    st.title("🖍️ Tempat Menggambar")
    
    st.write("Gunakan area di bawah ini untuk menggambar pohon rumah dan orang")
    
    # Pilihan warna dan ukuran kuas
    stroke_color = st.color_picker("Pilih warna kuas:", "#000000")
    stroke_width = st.slider("Ukuran kuas:", 1, 25, 5)
    
    # Tempat menggambar (canvas)
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 1)",  # warna latar belakang
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#FFFFFF",
        height=400,
        width=600,
        drawing_mode="freedraw",  # bisa diubah ke "rect", "circle", "line", dll.
        key="canvas",
    )
    
    # Jika pengguna sudah menggambar sesuatu
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data, caption="Hasil Gambar Anda")
    
        # Tombol untuk menyimpan gambar
        if st.button("💾 Simpan Gambar"):
            img = Image.fromarray((canvas_result.image_data).astype("uint8"))
            img.save("hasil_gambar.png")
            st.success("Gambar disimpan sebagai hasil_gambar.png")
    
    st.write("---")
    st.info("Gunakan mouse atau jari (jika di HP/tablet) untuk menggambar.")
with st.container():
    st.write("---")
    st.caption("agna aldhaka-contoh penggunaan cnn untuk deteksi gambar")
