import os
import pickle
import streamlit as st

# Menampilkan path file model untuk memastikan aksesnya
model_path = os.path.join(os.getcwd(), 'estimasi_mobil.sav')
st.write(f"Path file model: {model_path}")

# Coba memuat model dan penanganan error
try:
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    st.error(f"Model tidak ditemukan di path {model_path}. Pastikan file 'estimasi_mobil.sav' ada di direktori yang benar.")
    model = None
except Exception as e:
    st.error(f"Terjadi kesalahan saat memuat model: {e}")
    model = None

# Pastikan model berhasil dimuat sebelum melanjutkan
if model:
    st.title('Estimasi Harga Mobil Bekas')

    # Input dari pengguna
    year = st.number_input('Input Tahun Mobil')
    mileage = st.number_input('Input Km Mobil')
    tax = st.number_input('Input Pajak Mobil')
    mpg = st.number_input('Input Konsumsi BBM Mobil')
    engineSize = st.number_input('Input Engine Size')

    predict = ''

    if st.button('Estimasi Harga'):
        # Melakukan prediksi jika model sudah dimuat
        if model:
            predict = model.predict([[year, mileage, tax, mpg, engineSize]])  # Input model harus berupa array 2D
            st.write('Estimasi harga mobil bekas dalam Ponds: ', predict[0])
            st.write('Estimasi harga mobil bekas dalam IDR (juta): ', predict[0] * 19000)
        else:
            st.error("Model tidak dapat dijalankan karena kesalahan pemuatan model.")
