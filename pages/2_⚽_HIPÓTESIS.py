import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.hipot import hipotesis1
from src.hipot import hipotesis2
from src.hipot import hipotesis3
from src.hipot import hipotesis4
from src.hipot import hipotesis5
from src.hipot import hipotesis1_mosaico

#from matplotlib.backends.backend_agg import RendererAgg
#_lock = RendererAgg.lock

df = pd.read_csv("data/fifaPlayers4.csv")

st.header("PROYECTO FIFA PLAYERS - HIPÓTESIS")

opcion = st.selectbox(
    "Escoja la hipótesis a revisar: ",
    ["Seleccione hipótesis","Hipótesis 1","Hipótesis 2","Hipótesis 3","Hipótesis 4","Hipótesis 5"]
)

if opcion == "Hipótesis 1":
    st.html("<b>Relación entre las características físicas de los jugadores y su rendimiento.</b>")
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
    st.html("<b>Existe una relación entre la edad de los jugadores y su valor en el mercado.</b>")
    hipotesis2(df)
elif opcion == "Hipótesis 3":
    st.html("<b>Cuáles son los clubes que más invierten en jugadores.</b>")
    valorTop = st.slider(
        "Seleccione un valor de top",
        min_value=0,
        max_value=10,
        step=1,
        value=0
    )
    hipotesis3(df, valorTop)
elif opcion == "Hipótesis 4":
    st.html("<b>Relación entre ingresos y efectividad defensa-ataque.</b>")
    hipotesis4(df)
elif opcion == "Hipótesis 5":
    st.html("<b>La reputación internacional de un jugador tiene relación directa con sus ingresos.</b>")
    hipotesis5(df)





#def main():
#    pass
#if "__name__" == "__main__":
#    main()