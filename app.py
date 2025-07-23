# ====================================================================
# --- APLIKASI WEB PREDIKSI DIABETES DENGAN STREAMLIT (VERSI FINAL) ---
# ====================================================================

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- KONFIGURASI HALAMAN ---
# PENTING: st.set_page_config() harus menjadi perintah Streamlit pertama.
st.set_page_config(
    page_title="Prediksi Risiko Diabetes",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- FUNGSI UNTUK MEMUAT MODEL DAN SCALER ---
@st.cache_resource
def load_model_and_scaler():
    """Memuat model dan scaler yang sudah disimpan."""
    try:
        model = joblib.load('model_prediksi_diabetes.joblib')
        scaler = joblib.load('scaler_final.joblib')
        return model, scaler
    except FileNotFoundError as e:
        return None, None
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat file: {e}")
        return None, None

# Memuat model dan scaler di awal
final_model, scaler = load_model_and_scaler()

# --- ANTARMUKA APLIKASI WEB ---

st.title('Aplikasi Prediksi Risiko Diabetes 🩺')
st.write("""
Aplikasi ini memprediksi risiko diabetes pada seorang pasien berdasarkan beberapa atribut kesehatan.
Silakan masukkan data di bawah ini untuk memulai prediksi.
""")

# Cek apakah model dan scaler berhasil dimuat sebelum melanjutkan
if final_model is None or scaler is None:
    st.error("Gagal memuat file model atau scaler. Pastikan file 'model_prediksi_diabetes.joblib' dan 'scaler_final.joblib' berada di direktori yang sama dengan app.py.")
else:
    # --- INPUT DARI PENGGUNA ---
    st.header('Masukkan Data Pasien')

    try:
        feature_names = final_model.feature_names_in_
    except AttributeError:
        st.warning("Tidak dapat mendeteksi nama fitur dari model. Menggunakan daftar manual.")
        feature_names = ['Glucose', 'BMI', 'Age', 'BloodPressure', 'DiabetesPedigreeFunction'] # GANTI JIKA PERLU

    col1, col2 = st.columns(2)
    input_data = {}
    
    mid_point = (len(feature_names) + 1) // 2
    
    # Fungsi untuk membuat input field dengan validasi
    def create_input(feature):
        # Kondisi khusus untuk membatasi input DiabetesPedigreeFunction
        if feature == 'DiabetesPedigreeFunction':
            input_data[feature] = st.number_input(
                label=f'{feature}',
                min_value=0.0,
                max_value=1.0,  # <-- Batas atas diatur ke 1.0
                step=0.01,
                format="%.3f"
            )
        else:
            # Input standar untuk fitur lainnya
            input_data[feature] = st.number_input(
                label=f'{feature}',
                min_value=0.0, # Menambahkan batas bawah untuk semua
                step=1.0,
                format="%.1f"
            )

    # Menggunakan fungsi untuk membuat input di setiap kolom
    with col1:
        for feature in feature_names[:mid_point]:
            create_input(feature)
    with col2:
        for feature in feature_names[mid_point:]:
            create_input(feature)

    # Tombol untuk memicu prediksi
    if st.button('**Cek Prediksi Risiko**', type="primary", use_container_width=True):
        
        # --- LOGIKA PREDIKSI (DIPERBAIKI) ---

        # 1. Ubah input dictionary ke dalam DataFrame
        input_df = pd.DataFrame([input_data])
        input_df = input_df[feature_names]
        
        # 2. Lakukan scaling pada data input
        input_scaled_array = scaler.transform(input_df)
        
        # 3. Buat kembali DataFrame dengan nama kolom setelah scaling
        #    Ini adalah langkah untuk menghilangkan UserWarning
        input_scaled_df = pd.DataFrame(input_scaled_array, columns=feature_names)
        
        # 4. Lakukan prediksi menggunakan DataFrame yang sudah punya nama kolom
        prediction = final_model.predict(input_scaled_df)
        
        # 5. Tampilkan hasil prediksi
        st.subheader('Hasil Prediksi:')
        
        if prediction[0] == 0:
            st.success('**Risiko Rendah (Tidak Terdeteksi Diabetes)**')
        else:
            st.error('**Risiko Tinggi (Terdeteksi Diabetes)**')

# Menambahkan footer
st.markdown("---")
st.write("Dibuat dengan Streamlit | Model: Random Forest")
