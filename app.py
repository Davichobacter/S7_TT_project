import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Cargar los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un encabezado para la aplicación Streamlit
st.title('Relación entre Odómetro y Precio de Vehículos Usados')

# Filtro por rango de odómetro
odometer_min = int(car_data['odometer'].min())
odometer_max = int(car_data['odometer'].max())
odometer_range = st.slider(
    'Rango de odómetro:',
    odometer_min,
    odometer_max,
    (odometer_min, odometer_max)
)

# Filtro por rango de precio
price_min = int(car_data['price'].min())
price_max = int(car_data['price'].max())
price_range = st.slider(
    'Rango de precio:',
    price_min,
    price_max,
    (price_min, price_max)
)

# Filtro por tipo de transmisión
transmission_options = ['all'] + \
    sorted(car_data['transmission'].dropna().unique().tolist())
transmission_type = st.selectbox(
    'Tipo de transmisión:',
    options=transmission_options
)

# Filtro por condición del vehículo
condition_options = sorted(car_data['condition'].dropna().unique().tolist())
selected_condition = st.multiselect(
    'Condición del vehículo:',
    options=condition_options,
    default=condition_options
)

# Aplicar filtros al DataFrame
filtered_data = car_data[
    (car_data['odometer'] >= odometer_range[0]) &
    (car_data['odometer'] <= odometer_range[1]) &
    (car_data['price'] >= price_range[0]) &
    (car_data['price'] <= price_range[1]) &
    (car_data['condition'].isin(selected_condition))
]

if transmission_type != 'all':
    filtered_data = filtered_data[filtered_data['transmission']
                                  == transmission_type]

st.write(f"Vehículos encontrados: {len(filtered_data)}")

# Crear un scatter plot interactivo utilizando plotly.graph_objects
fig = go.Figure(
    data=[
        go.Scatter(
            x=filtered_data['odometer'],
            y=filtered_data['price'],
            mode='markers',
            marker=dict(
                size=8,
                opacity=0.6
            ),
            text=filtered_data['condition'],
            hovertemplate=(
                'Odómetro: %{x}<br>' +
                'Precio: %{y}<br>' +
                'Condición: %{text}<extra></extra>'
            )
        )
    ]
)

fig.update_layout(
    title_text='Relación entre Odómetro y Precio (con filtros)',
    xaxis_title='Odómetro',
    yaxis_title='Precio'
)

# Mostrar el gráfico en la aplicación Streamlit
st.plotly_chart(fig, use_container_width=True)

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
