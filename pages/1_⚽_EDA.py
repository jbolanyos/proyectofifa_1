import streamlit as st
import pandas as pd

st.header("PROYECTO FIFA PLAYERS - ANÁLISIS EXPLORATORIO DE DATOS")

df = pd.read_csv("data/fifaPlayers4.csv")

with st.container():
    col1, col2 = st.columns([0.3,0.7])
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
            st.text("Sobre el conjunto de datos:*")
            st.text("El Data Set FIFA Players es una colección de información detallada sobre jugadores, equipos y ligas de FIFA. Proporciona una visión holística de la representación de las estadísticas de fútbol de la FIFA en el juego e incluye atributos clave para jugadores individuales, equipos de clubes y ligas de varios países.")
            st.text("Especificamente para este proyecto se utiliza la fuente de fifa_players.csv el cual contiene atributos individuales del jugador, como la calificación general, el potencial, el físico, las habilidades y los rasgos.")
            st.text("Asimismo, incluye detalles como la altura, el peso, la afiliación al club y varias métricas técnicas (por ejemplo, regates, remates, pases y defensas)")
            st.text("Enlace a Kaggle: https://www.kaggle.com/datasets/moradi/fifa-stats")
            st.text("")
            st.text("*Información extraída de la página de Kaggle del Data Set")

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