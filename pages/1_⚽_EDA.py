import streamlit as st
import pandas as pd

st.header("PROYECTO FIFA - ANÁLISIS EXPLORATORIO DE DATOS")

df = pd.read_csv("data/fifaPlayers4.csv")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        respuesta = st.radio(
            "Seleccione información:",
            ["Sobre el DataFrame", "Número de registros","Número de columnas","Columnas","Edad de los jugadores", 
            "Altura de los jugadores", "Peso de los jugadores"]
        )
    
    with col2:
        if respuesta == "Número de registros":
            st.metric("Número de registros", df.shape[0])
        elif respuesta == "Número de columnas":
            st.metric("Número de columnas", df.shape[1])
        elif respuesta == "Columnas":
            st.subheader("Las columnas del DataFrame son:")
            st.table(list(df.columns))
        elif respuesta == "Sobre el DataFrame":
            st.text("Sobre el DataFrame")
        elif respuesta == "Edad de los jugadores":
            st.subheader("Métricas:")
            st.table(df['Age'].describe())
        elif respuesta == "Altura de los jugadores":
            st.subheader("Métricas:")
            st.table(df['Height'].describe())
        elif respuesta == "Peso de los jugadores":
            st.subheader("Métricas:")
            st.table(df['Weight'].describe())

#st.header("ANALISIS EXPLORATORIO")

#with st.container():
#    col1, col2, col3 = st.columns(3)
#    with col1:
#        st.metric(label="Número de filas:", value=df.shape[0], border=True)


#st.table(df.head(5))