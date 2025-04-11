import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Data model
tahun = np.array([2016, 2017, 2018, 2019, 2020]).reshape(-1, 1)
harga = np.array([200, 220, 240, 260, 280])  # juta

model = LinearRegression()
model.fit(tahun, harga)

# UI
st.title("Prediksi Harga Rumah AI")
st.write("Masukkan tahun untuk memprediksi harga:")

input_tahun = st.number_input("Tahun", min_value=2010, max_value=2030, step=1)

if st.button("Prediksi"):
    prediksi = model.predict([[input_tahun]])
    st.success(f"Prediksi harga rumah di tahun {input_tahun}: {prediksi[0]:.2f} juta")