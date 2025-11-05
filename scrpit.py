import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import pandas as pd
import os

print('My working directory is', os.getcwd())

x = 10

if x % 2 == 0:
    print(f'{x} is an even number')
else:
    print(f'{x} is an odd number')


# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un scatter plot utilizando plotly.graph_objects
# Se crea una figura vacía y luego se añade un rastro de scatter
fig = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                y=car_data['price'], mode='markers')])

# Opcional: Puedes añadir un título al gráfico si lo deseas
fig.update_layout(title_text='Relación entre Odómetro y Precio')

# Mostrar el gráfico Plotly
fig.show()
