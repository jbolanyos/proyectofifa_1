import streamlit as st
import pandas as pd
from src.model import entrenar

st.header("PROYECTO FIFA - MODELO DE MACHINE LEARNING")

df = pd.read_csv("data/fifaPlayers4.csv")

coltarget = st.selectbox(
    "Seleccione target:",
    ["Velocidad","Control del balón"]
)

if coltarget == "Velocidad": 
    entrenar(df, 'Sprint speed')
elif coltarget == "Control del balón": 
    entrenar(df, 'Ball control')

