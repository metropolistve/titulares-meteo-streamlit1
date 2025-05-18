
import streamlit as st
import pandas as pd

# Cargar datos desde CSV
@st.cache_data
def cargar_datos():
    df = pd.read_csv("dataset_meteostat_madrid_castellano.csv", parse_dates=['fecha'])
    return df

df = cargar_datos()

# Título e instrucciones
st.title("📰 Generador de Titulares Meteorológicos")
st.markdown("Consulta un titular informativo para una fecha concreta en Madrid, basado en datos reales de Meteostat.")

# Selector de fecha
fecha = st.date_input("Selecciona una fecha", min_value=df['fecha'].min(), max_value=df['fecha'].max())

# Selector de parámetro
parametro = st.selectbox("Selecciona un parámetro", [
    "temperatura máxima", "temperatura mínima", "precipitación", "racha de viento"
])

# Buscar fila correspondiente
fila = df[df['fecha'] == pd.to_datetime(fecha)]

if not fila.empty:
    row = fila.iloc[0]
    if parametro == "temperatura máxima" and row['temperatura_maxima'] >= 30:
        st.success(f"Madrid supera los {row['temperatura_maxima']}°C el {fecha.strftime('%-d de %B')}")
    elif parametro == "temperatura mínima" and row['temperatura_minima'] <= 3:
        st.success(f"Noches frías en Madrid con {row['temperatura_minima']}°C el {fecha.strftime('%-d de %B')}")
    elif parametro == "precipitación" and row['precipitacion'] > 0:
        st.success(f"Ha llovido {row['precipitacion']} mm en Madrid el {fecha.strftime('%-d de %B')}")
    elif parametro == "racha de viento" and row['racha_viento'] >= 50:
        st.success(f"Viento fuerte en Madrid el {fecha.strftime('%-d de %B')} con ráfagas de {row['racha_viento']} km/h")
    else:
        st.info("No se han registrado fenómenos destacados ese día para el parámetro seleccionado.")
else:
    st.warning("Fecha no disponible en el dataset.")
