import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.hipot import hipotesis1
from src.hipot import hipotesis1_mosaico

#from matplotlib.backends.backend_agg import RendererAgg
#_lock = RendererAgg.lock

df = pd.read_csv("data/fifaPlayers4.csv")

st.header("PROYECTO FIFA-HIPÓTESIS")

opcion = st.selectbox(
    "Escoja la hipótesis a revisar: ",
    ["Seleccione hipótesis","Hipótesis 1","Hipótesis 2","Hipótesis 3","Hipótsis 4","Hipótesis 5"]
)

if opcion == "Hipótesis 1":
    st.html("<b>¿Cuál es el grado de influencia de las características físicas de los jugadores en su desempeño en la cancha?</b>")
    col1, col2 = st.columns([0.50,0.50])
    with col1:
        tamanyo = st.slider("Número de muestra", 0, 200, step=10, value=100)
    with col2:
        salida = st.selectbox(   
            "Seleccione información:",
             ["Efectividad de ataque","Efectividad de defensa","Agilidad",'Control del balón','Movimiento en cancha','Velocidad','Valoración General']
        )
    
    col3, col4 = st.columns([0.50, 0.50])
    with col3:
        st.text("Por estatura y peso:")
        hipotesis1(df,tamanyo,salida)
    with col4:
        st.text("Por el tipo de cuerpo (Delgado, Normal, Robusto):")    
        hipotesis1_mosaico(df,salida)

elif opcion == "Hipótesis 2":
    st.text("Esta es la hipótesis 2")
elif opcion == "Hipótesis 3":
    st.text("Esta es la hipótesis 3")
elif opcion == "Hipótesis 4":
    st.text("Esta es la hipótesis 4")
elif opcion == "Hipótesis 5":
    st.text("Esta es la hipótesis 5")


#def main():
#    pass
#if "__name__" == "__main__":
#    main()