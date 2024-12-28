import streamlit as st
import pandas as pd
from src.model import entrenar
from src.model import graficar_modelo
from src.model import probar_modelo_1

st.header("PROYECTO FIFA PLAYERS - MODELO ML SUPERVISADO")

df = pd.read_csv("data/fifaPlayers4.csv")

coltarget = st.selectbox(
    "Target:",
    ["Selecciona característica a analizar",
     "Velocidad",
     "Control del balón",
     "Drible",
     "Pases largos",
     "Movimiento en cancha",
     "Aceleración",
     "Agilidad",
     "Equilibrio",
     "Reacción",
     "Fuerza de disparo",
     "Salto",
     "Resistencia",
     "Fuerza física",
     "Disparos largos"
     ]
)

col1, col2 = st.columns([0.4,0.6])

with col1:
    if coltarget == "Velocidad": ganador = entrenar(df, 'Sprint speed')
    elif coltarget == "Control del balón": ganador = entrenar(df, 'Ball control')
    elif coltarget == "Drible": ganador = entrenar(df, 'Dribbling')
    elif coltarget == "Pases largos": ganador = entrenar(df, 'Long passing')
    elif coltarget == "Movimiento en cancha": ganador = entrenar(df, 'Total movement')
    elif coltarget == "Aceleración": ganador = entrenar(df, 'Acceleration')
    elif coltarget == "Agilidad": ganador = entrenar(df, 'Agility')
    elif coltarget == "Equilibrio": ganador = entrenar(df, 'Balance')
    elif coltarget == "Reacción": ganador = entrenar(df, 'Reactions')    
    elif coltarget == "Fuerza de disparo": ganador = entrenar(df, 'Shot power')
    elif coltarget == "Salto": ganador = entrenar(df, 'Jumping')
    elif coltarget == "Resistencia": ganador = entrenar(df, 'Stamina')
    elif coltarget == "Fuerza física": ganador = entrenar(df, 'Strength')
    elif coltarget == "Disparos largos": ganador = entrenar(df, 'Long shots')

with col2:
    if coltarget != "Selecciona característica a analizar":
        st.write("Variable más influyente:", ganador[0])
        #st.write(ganador)
        graficar_modelo(ganador[1],ganador[0],coltarget)
        #probar_modelo_1(ganador[1],ganador[0])