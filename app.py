import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Cargar los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado para la aplicación Streamlit
st.title('Relación entre Odómetro y Precio de Vehículos Usados')

# Crear un scatter plot utilizando plotly.graph_objects
fig = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                y=car_data['price'], mode='markers')])
fig.update_layout(title_text='Relación entre Odómetro y Precio')

# Mostrar el gráfico en la aplicación Streamlit
st.plotly_chart(fig)

# Crear un histograma del precio de los vehículos
st.subheader('Distribución de Precios de Vehículos Usados')

# Crear el histograma utilizando plotly.graph_objects
hist_fig = go.Figure(data=[go.Histogram(x=car_data['price'], nbinsx=50)])
hist_fig.update_layout(title_text='Histograma de Precios de Vehículos Usados')

# Mostrar el histograma en la aplicación Streamlit
st.plotly_chart(hist_fig)

# Crear un filtro para el rango de precios
st.subheader('Filtrar Vehículos por Rango de Precio')
price_range = st.slider('Selecciona el rango de precios:',
                        int(car_data['price'].min()),
                        int(car_data['price'].max()),
                        (int(car_data['price'].min()), int(car_data['price'].max())))


# Crear botón para seleccionar el tipo de transmisión
transmission_type = st.selectbox('Selecciona el tipo de transmisión:',
                                 options=['all', 'automatic', 'manual'])

# Crear selector para la condición del vehículo
condition_options = car_data['condition'].unique().tolist()
selected_condition = st.multiselect(
    'Selecciona la condición del vehículo:', options=condition_options, default=condition_options)


# Crear un botón para mostrar los datos filtrados
if st.button('Mostrar datos filtrados'):
    filtered_data = car_data[(car_data['price'] >= price_range[0]) & (
        car_data['price'] <= price_range[1])]
    if transmission_type != 'all':
        filtered_data = filtered_data[filtered_data['transmission']
                                      == transmission_type]
    filtered_data = filtered_data[filtered_data['condition'].isin(
        selected_condition)]
    st.dataframe(filtered_data)
    st.write(
        f'Se encontraron {len(filtered_data)} vehículos que cumplen con los criterios de filtrado.')

# Fin de la aplicación Streamlit
