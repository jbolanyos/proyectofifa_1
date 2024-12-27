import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
import plotly.figure_factory as ff
import seaborn as sns
from statsmodels.graphics.mosaicplot import mosaic

def normalizarCampo(datax,campox):
    datax[campox] = pd.to_numeric(datax[campox], errors='coerce')
    datax = datax.dropna(subset=[campox])
    datax[campox]=datax[campox].astype(int) 
    minimo = datax[campox].min()
    maximo = datax[campox].max()
    mitad = (minimo + maximo) / 2
    segundo = (minimo + mitad) / 2
    tercero = (mitad + maximo) / 2
    limites = [minimo,segundo,tercero,maximo]
    return datax, limites    

def hipotesis1(data,muestra,salida):
    campox = ''
    datax = data.loc[:,['Age','Height','Weight','Body type','Attacking work rate','Defensive work rate','Total skill','Agility','Ball control','Total movement','Sprint speed']]        
    if salida=='Valoración General':
        campox = 'Total skill'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasPotencial'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasPotencial'
    elif salida=='Efectividad de ataque':
        campox = 'Attacking work rate'
    elif salida=='Efectividad de defensa':
        campox='Defensive work rate'
    elif salida=='Agilidad':
        campox = 'Agility'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasAgilidad'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasAgilidad'
    elif salida=="Control del balón":
        campox = 'Ball control'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasBallControl'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasBallControl'
    elif salida=="Movimiento en cancha":
        campox = 'Total movement'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasMovilidad'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasMovilidad'
    elif salida == "Velocidad":
        campox = 'Sprint speed'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasVelocidad'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasVelocidad'
    fig, ax = plt.subplots()
    sns.scatterplot(
        x='Height',
        y='Weight',
        hue=campox,
        #data=subset3.head(muestra)
        data=datax.head(muestra)
    )
    #plt.show()
    st.pyplot(fig)
    
def hipotesis1_mosaico(data,salida):
    campox = ''
    datax = data.loc[:,['Age','Height','Weight','Body type','Attacking work rate','Defensive work rate','Total skill','Agility','Ball control','Total movement','Sprint speed']]        
    if salida=='Valoración General':
        campox = 'Total skill'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasPotencial'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasPotencial'
    elif salida=='Efectividad de ataque':
        campox = 'Attacking work rate'
    elif salida=='Efectividad de defensa':
        campox='Defensive work rate'
    elif salida=='Agilidad':
        campox = 'Agility'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasAgilidad'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasAgilidad'
    elif salida=="Control del balón":
        campox = 'Ball control'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasBallControl'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasBallControl'
    elif salida=="Movimiento en cancha":
        campox = 'Total movement'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasMovilidad'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasMovilidad'
    elif salida == "Velocidad":
        campox = 'Sprint speed'
        datax, limites = normalizarCampo(datax,campox)
        datax['categoriasVelocidad'] = pd.cut(datax[campox], bins=limites, labels=['Baja','Media','Alta'])
        campox = 'categoriasVelocidad'
    
    datax['TipoCuerpo'] = datax['Body type'].str.split("(").str[0]
    
    # Create mosaic plot from DataFrame
    fig, _ =mosaic(datax, ['TipoCuerpo', campox])
    st.pyplot(fig)
