import sklearn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

global modelo 

def normalizar(datax, indice):
    datax[indice] = pd.to_numeric(datax[indice], errors='coerce')
    datax = datax.dropna(subset=[indice])
    datax[indice]=datax[indice].astype(int) 
    return datax

def hacerRegresion(datax,entrada,coltarget):
    x = datax[entrada]
    y = datax[coltarget]
    modelo = LinearRegression()
    modelo.fit(x.values.reshape(-1, 1), y)
    dependencia = modelo.score(x.values.reshape(-1, 1), y)
    #pendiente = modelo.coef_
    #intersecto = modelo.intercept
    return dependencia

def entrenar(data, coltarget):
    listaCampos = ['Age','Height','Weight','Sprint speed','Ball control','Dribbling',
                   'Long passing','Total movement','Acceleration','Agility','Balance',
                   'Reactions','Shot power','Jumping','Stamina','Strength','Long shots'
                   ]
    datax = data.loc[:,listaCampos]
    nCols = datax.shape[1]
    campos = range(nCols)
    for i in campos:
        datax = normalizar(datax,listaCampos[i])
    
    coeficientes = pd.DataFrame(columns=['variable','influencia'])
    
    for i in campos:
        entrada = listaCampos[i]
        if entrada != coltarget:
            dependencia = hacerRegresion(datax,entrada,coltarget)
            coeficientes.loc[len(coeficientes)]=[entrada, dependencia]
    
    st.text("Influencia de las variables:")
    coeficientes = coeficientes.sort_values('influencia',ascending=False)
    st.table(coeficientes)
    return [coeficientes.iloc[0]['variable'],datax,dependencia]

def conversorColumna(coltarget):
    campox = ''
    if coltarget == "Velocidad": campox = 'Sprint speed'
    elif coltarget == "Control del balón": campox = 'Ball control'
    elif coltarget == "Drible": campox = 'Dribbling'
    elif coltarget == "Pases largos": campox = 'Long passing'
    elif coltarget == "Movimiento en cancha": campox = 'Total movement'
    elif coltarget == "Aceleración": campox = 'Acceleration'
    elif coltarget == "Agilidad": campox = 'Agility'
    elif coltarget == "Equilibrio": campox = 'Balance'
    elif coltarget == "Reacción": campox = 'Reactions'
    elif coltarget == "Fuerza de disparo": campox = 'Shot power'
    elif coltarget == "Salto": campox = 'Jumping'
    elif coltarget == "Resistencia": campox = 'Stamina'
    elif coltarget == "Fuerza física": campox = 'Strength'
    elif coltarget == "Disparos largos": campox = 'Long shots'
    
    return campox

def graficar_modelo(datax, variable, coltarget):
    #x = datax[variable]
    y = datax[conversorColumna(coltarget)]
    #fig,_ = plt.scatter(x,y)
    fig, ax = plt.subplots()
    p1=sns.scatterplot(
        x=variable,
        y=conversorColumna(coltarget),
        data=datax.head(100),
        ax=sns.regplot(data=datax.head(100), x=variable, y=conversorColumna(coltarget), line_kws={'color': 'g'})
    )
    st.pyplot(fig)

def probar_modelo_1(datax, variable):
    pass
    #datosPredictY = modelo.predict(datax[variable])
    
    #fig, ax = plt.subplots()
    #datosPlot = pd.DataFrame(columns=['x_','y_'])
    #datosPlot['x_'] = datax[variable]
    #datosPlot['y_'] = datosY
    #p1=sns.scatterplot(
    #    x='x_',
    #    y='y_',
    #    data=datosPlot.head(100),
    #    ax=sns.regplot(data=datosPlot.head(100), x='x_', y='y_', line_kws={'color': 'g'})
    #)
    #st.pyplot(fig)