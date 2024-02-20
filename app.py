import pandas as pd
import plotly_express as px
import streamlit as st

st.header('Anúncios de vendas de carros')

car_data = pd.read_csv('vehicles_us.csv')
build_histogram = st.checkbox('Criar um histograma')
if build_histogram:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')


    fig = px.histogram(car_data, x = 'odometer')

    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar gráfico de dispersão')
if build_scatter:
    st.write('Criando gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    fig = px.scatter(car_data, x = 'odometer', y = 'price')

    st.plotly_chart(fig, use_container_width=True)

