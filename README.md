# S7_TT_project

Esta aplicación interactiva, desarrollada con Streamlit y Plotly, permite explorar y visualizar datos de vehículos usados, mostrando la relación entre el kilometraje (odómetro), el precio y otras características como la transmisión y condición del vehículo.

## Características principales

Visualización interactiva:
Muestra gráficos dinámicos de dispersión y de histograma usando plotly.graph_objects.

Filtros personalizables:
Permite filtrar los vehículos por:

Rango de precios (mediante un control deslizante)

Tipo de transmisión (automatic, manual, o all)

Condición del vehículo (según las categorías disponibles en el dataset)

Exploración de datos:
Los resultados filtrados se presentan en una tabla interactiva, junto con el número total de registros que cumplen con los criterios seleccionados.

## Tecnologías utilizadas

Python 3.x

Streamlit

Pandas

Plotly

## Estructura del proyecto
```
.
├── vehicles_us.csv
├── app.py
└── README.md
```

## Instalación y ejecución

Clona este repositorio:

```
git clone https://github.com/Davichobacter/S7_TT_project
cd S7_TT_project
```


Crea un entorno virtual (opcional pero recomendado):

```
python -m venv venv
source venv/bin/activate   # En macOS / Linux
venv\Scripts\activate      # En Windows
```

Instala las dependencias:

```
pip install -r requirements.txt
```

Si no tienes el archivo requirements.txt, puedes instalar los paquetes manualmente:

```
pip install pandas plotly streamlit
```

Ejecuta la aplicación:

```
streamlit run app.py
```

Abre tu navegador en:

http://localhost:8501

## Funcionalidades del código

Gráfico de dispersión: Muestra la relación entre el odómetro y el precio de los vehículos.

Histograma de precios: Visualiza la distribución de los precios.

Filtros dinámicos: Permite seleccionar rango de precios, tipo de transmisión y condición del vehículo.

Resultados interactivos: Muestra una tabla de datos filtrados con el número total de coincidencias.

## Dataset

El archivo vehicles_us.csv contiene información sobre vehículos usados, incluyendo:

- price: precio del vehículo.
- odometer: kilometraje registrado.
- transmission: tipo de transmisión.
- condition: estado del vehículo.