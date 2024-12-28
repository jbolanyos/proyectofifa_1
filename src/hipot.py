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
        data=datax.head(muestra)
    )
    
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

def hipotesis2(data):
    df = data.loc[:,['Age','Value','Wage','Release clause']]
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    df = df.dropna(subset=['Age'])
    df['Age']=df['Age'].astype(int)

    df['Value'] = df['Value'].str.split("€").str[1]
    df['Value'] = df['Value'].str.replace('K','000')
    df['Value'] = df['Value'].str.replace('M','000000')
    df['Value'] = df['Value'].str.replace('.','')

    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

    fig, ax = plt.subplots()
    df.groupby('Age')['Value'].mean().plot(kind='bar', rot=45, fontsize=10, figsize=(8, 6))
    ax.legend(['Valor en mercado'])
    st.pyplot(fig)

def hipotesis3(data, valorTop):
    if (valorTop > 0):
        df = data.loc[:,['club_name','Value']]
        df['Value'] = df['Value'].str.split("€").str[1]
        df['Value'] = df['Value'].str.replace('K','000')
        df['Value'] = df['Value'].str.replace('M','000000')
        df['Value'] = df['Value'].str.replace('.','')
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

        dfMuestra = df.groupby('club_name')['Value'].mean()
        dfMuestra = dfMuestra.sort_values(ascending=False)

        fig, ax = plt.subplots()
        dfMuestra.head(valorTop).plot(kind='bar', rot=45, fontsize=10, figsize=(8, 6))
        st.pyplot(fig)

def hipotesis4(data):
    dfh4 = data.loc[:,['Attacking work rate','Defensive work rate','Value']]

    dfh4['Value'] = dfh4['Value'].str.split("€").str[1]
    dfh4['Value'] = dfh4['Value'].str.replace('K','000')
    dfh4['Value'] = dfh4['Value'].str.replace('M','000000')
    dfh4['Value'] = dfh4['Value'].str.replace('.','')
    dfh4['Value'] = pd.to_numeric(dfh4['Value'], errors='coerce')

    dfMuestrah4_1 = dfh4.groupby('Attacking work rate')['Value'].mean()
    dfMuestrah4_1 = dfMuestrah4_1.sort_values(ascending=False)

    dfMuestrah4_2 = dfh4.groupby('Defensive work rate')['Value'].mean()
    dfMuestrah4_2 = dfMuestrah4_2.sort_values(ascending=False)

    fig, ax = plt.subplots()
    dfMuestrah4_1.plot(kind='bar', rot=45, fontsize=10, figsize=(8, 6))
    ax.legend(['Valor en mercado'])
    st.pyplot(fig)

    fig, ax = plt.subplots()
    dfMuestrah4_2.plot(kind='bar', rot=45, fontsize=10, figsize=(8, 6))
    ax.legend(['Valor en mercado'])
    st.pyplot(fig)

def hipotesis5(data):
    dfh5 = data.loc[:,['International reputation','Value']]

    dfh5['Value'] = dfh5['Value'].str.split("€").str[1]
    dfh5['Value'] = dfh5['Value'].str.replace('K','000')
    dfh5['Value'] = dfh5['Value'].str.replace('M','000000')
    dfh5['Value'] = dfh5['Value'].str.replace('.','')
    dfh5['Value'] = pd.to_numeric(dfh5['Value'], errors='coerce')

    dfMuestrah5 = dfh5.groupby('International reputation')['Value'].mean()
    dfMuestrah5 = dfMuestrah5.sort_values(ascending=False)

    fig, ax = plt.subplots()
    dfMuestrah5.plot(kind='bar', rot=45, fontsize=10, figsize=(8, 6))
    ax.legend(['Valor en mercado'])
    st.pyplot(fig)