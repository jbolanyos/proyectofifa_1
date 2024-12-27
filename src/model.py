import sklearn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def normalizar(datax, indice):
    datax[indice] = pd.to_numeric(datax[indice], errors='coerce')
    datax = datax.dropna(subset=[indice])
    datax[indice]=datax[indice].astype(int) 
    return datax

def hacerRegresion(datax,entrada,coltarget):
    x = datax[entrada]
    y = datax[coltarget]
    model = LinearRegression()
    model.fit(x.values.reshape(-1, 1), y)
    dependencia = model.score(x.values.reshape(-1, 1), y)
    return dependencia

def entrenar(data, coltarget):
    listaCampos = ['Age','Height','Weight','Sprint speed','Ball control']
    datax = data.loc[:,listaCampos]        
    nCols = datax.shape[1]
    campos = range(nCols)
    for i in campos:
        datax = normalizar(datax,listaCampos[i])
    
    coeficientes = pd.DataFrame(columns=['insumo','valores'])
    #df = pd.DataFrame(columns=['first_name', 'last_name', 'gender'])
    
    for i in campos:
        entrada = listaCampos[i]
        if entrada != coltarget:
            dependencia = hacerRegresion(datax,entrada,coltarget)
            #tam = coeficientes['valor'].shape[0]
            #coeficientes.shape[0]
            #coeficientes[tam] = dependencia
            coeficientes.loc[len(coeficientes)]=[entrada, dependencia]
    
    st.text("Grado de influencia de las variables:")
    coeficientes = coeficientes.sort_values('valores',ascending=False)
    st.table(coeficientes)
    