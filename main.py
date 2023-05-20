import yfinance as yf
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt


st.write("""mi_app_activos
""")
symbolo = "GOOGL"
obtener_datos = yf.Ticker(symbolo)
periodo_datos = obtener_datos.history(period="1d", start = "2021-01-01", end = "2023-05-11")

datos = yf.download("GOOGL", start = "2021-01-01", end = "2023-05-11")
datos.to_csv("Datos_GOOGLE.csv")
plt.plot(datos["Close"])
plt.xlabel("Fecha")
plt.ylabel("Precios")
plt.title("Acciones GOOGLE")
plt.show()

print(datos.head())
st.line_chart(periodo_datos.Close)
st.line_chart(periodo_datos.Volume)
