import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



st.write("""Mi pequeña App de precios
mostrando las acciones de cierre  y volumen de APPLE""")

Symbolo = 'APPLE'

obtener_datos = yf.Ticker(Symbolo)
periodo_de_datos = obtener_datos.history(period='Id', start="2020-01-01", end="2023-05-06")

datos = yf.download("AAPL", start="2020-01-01", end="2023-05-06")
datos.to.csv('mis_datos_apple.csv')

plt.plot(datos['Close'])

plt.xlabel('Fecha')
plt.ylabel('Precio de cierre')
plt.title('Precio de cierre de las acciones de APPLE')
plt.show()

print(datos.head())
st.line_chart(periodo_de_datos.Close)
st.line_chart(periodo_de_datos.Volume)