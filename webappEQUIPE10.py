#libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import pandas as pd
import altair as alt
from urllib.error import URLError

#DÚVIDAS
rD = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vRtt6VlUfp77JA2ok1dUAN5WMj3NNKCliMyG6Tb7Yu8MzUzQ5lZXjcNOWMgit6VaJw8W8lPIzjjnWVn/pub?gid=51090662&single=true&output=csv')
dataD = rD.content
dfD = pd.read_csv(BytesIO(dataD), index_col=0)
NregD = len(dfD)
dfD.columns = ['email', 'equipe', 'nome', 'duvida', 'obs']
selecao10D = dfD['equipe']=='Equipe 10'
df10D = dfD[selecao10D]

#RESPOSTAS
rR = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQw6XD9vI_C4zvZ6W51vut_Ze_D_OSESuXiHh1IAXeBFXRRvyQ7kyFTLbGip1obadjbZHUmaAxvXmnz/pub?gid=1789345467&single=true&output=csv')
dataR = rR.content
dfR = pd.read_csv(BytesIO(dataR), index_col=0)
NregR = len(dfR)
dfR.columns = ['email', 'equipe', 'nome', 'resposta', 'sugestao']
selecao10R = dfR['equipe']=='Equipe 10'
df10R = dfR[selecao10R]

#Cálculo do Número de Registros por EQUIPE
NregDf10D = len(df10D)
NregDf10R = len(df10R)


image01 = Image.open('ImagemLateral.jpg')
st.sidebar.image(image01, width=300, caption='Mack Week CCT 2022') 
st.title("PAINEL - EQUIPE 10")
menu = ["Dúvidas",
        "Respostas",
        "Dúvidas e Respostas"]
choice = st.sidebar.selectbox("Menu de Opções",menu)
st.sidebar.info("By: Prof. Massaki de O. Igarashi")

if choice == "Dúvidas": 
    st.header("Relatório de DÚVIDAS")   
    st.write('EQUIPE 10:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df10D['duvida']) 
           
elif choice == "Respostas":       
    st.header("Relatório de RESPOSTAS")    
    st.write('EQUIPE 10:')    
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df10R['resposta'])  

               
elif choice == "Dúvidas e Respostas":       
    st.header("Relatório: DÚVIDAS E RESPOSTAS")  
    colDR1, colDR2 = st.columns((1,1))
    with colDR1:
        st.write("Nº TOTAL de Dúvidas (DESTA EQUIPE):")
        st.warning(NregDf10D)
    with colDR2:
        st.write("Nº TOTAL de dúvidas RESPONDIDAS:")
        st.info(NregDf10R)
    st.subheader('EQUIPE 10:')
    st.warning('Dúvida(s) Enviada(s)')
    st.code(df10D['duvida']) 
    st.info('Resposta do(a) TUTOR(A):')
    st.code(df10R['resposta'])  
