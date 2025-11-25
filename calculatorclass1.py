import streamlit as st

st.title("🧮 Kalkulator Sederhana")

st.write("Masukkan dua angka lalu pilih operasi yang diinginkan.")

# Input angka
angka1 = st.number_input("Angka pertama", value=0.0)
angka2 = st.number_input("Angka kedua", value=0.0)

# Pilih operasi
operasi = st.selectbox(
    "Pilih operasi",
    ("Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)")
)

# Tombol hitung
if st.button("Hitung"):
    if operasi == "Tambah (+)":
        hasil = angka1 + angka2
        st.success(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif operasi == "Kurang (-)":
        hasil = angka1 - angka2
        st.success(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif operasi == "Kali (×)":
        hasil = angka1 * angka2
        st.success(f"Hasil: {angka1} × {angka2} = {hasil}")
    elif operasi == "Bagi (÷)":
        if angka2 == 0:
            st.error("Error: Pembagian dengan nol tidak diperbolehkan.")
        else:
            hasil = angka1 / angka2
            st.success(f"Hasil: {angka1} ÷ {angka2} = {hasil}")
