import streamlit as st

st.header("PROYECTO FIFA PLAYERS - CONCLUSIONES")

col1,col2 = st.columns([0.2,0.8])
with col1:
    st.subheader("1:")
with col2:
    st.text("Las características físicas de los jugadores no tienen una influencia significativa en su rendimiento.")

col1,col2 = st.columns([0.2,0.8])
with col1:
    st.subheader("2:")
with col2:
    st.text("El mayor valor en el mercado de los jugadores se presenta entre las edades de 20 a 30 años.")

col1,col2 = st.columns([0.2,0.8])
with col1:
    st.subheader("3:")
with col2:
    st.text("Los clubes que invierten más en jugadores se encuentran en Europa")

col1,col2 = st.columns([0.2,0.8])
with col1:
    st.subheader("4:")
with col2:
    st.text("Los jugadores que presentan mayor efectividad tanto en defensa como ataque son quienes tienen promedio de salario más elevados.")

col1,col2 = st.columns([0.2,0.8])
with col1:
    st.subheader("5:")
with col2:
    st.text("Existe una relación directa entre la reputación internacional de un jugador y su valor en el mercado.")

col1,col2 = st.columns([0.2,0.8])
with col1:
    st.subheader("6:")
with col2:
    st.text("El modelo de aprendizaje supervisado permite determinar el grado de influencia entre diversas variables de los datos de los jugadores, como por ejemplo, determinar qué tanto influye la velocidad de un jugador en su resistencia en la cancha.")

st.html("<h2><b>Esta ha sido una pequeña muestra de las posibilidades de convertir los datos del fútbol en oportunidades. El llamado es a desarrollar proyectos locales que incentiven a los interesados en utilizar esta información como apoyo en sus decisiones o iniciativas.</b></h2>")
