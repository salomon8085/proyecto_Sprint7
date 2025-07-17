import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Título principal
st.title('Análisis de Anuncios de Vehículos en EE.UU.')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Checkbox para histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Distribución del Odómetro')
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'], marker_color='blue')])
    fig_hist.update_layout(
        title='Distribución del Odómetro',
        xaxis_title='Kilometraje (odometer)',
        yaxis_title='Frecuencia'
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión (Precio vs Kilometraje)'):
    st.write('Relación entre Precio y Kilometraje')
    fig_scatter = go.Figure(data=go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(color='blue', opacity=0.5)
    ))
    fig_scatter.update_layout(
        title='Relación entre Precio y Kilometraje',
        xaxis_title='Kilometraje (odometer)',
        yaxis_title='Precio (USD)'
    )
    st.plotly_chart(fig_scatter, use_container_width=True)