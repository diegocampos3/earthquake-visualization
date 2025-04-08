from pathlib import Path
import json
import plotly.express as px

# Leer los datos como una cadena y convertirlo en un objeto Python

path = Path('eq_data\\eq_data_30_day_m1.geojson')
contenst = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contenst)


# Crear una versión más legible del archivo de datos
path = Path('eq_data\\reable_eq_data.geojson')
reable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(reable_contents, encoding='utf-8') 

# Analizar todos los terremotos del conjunto de datos

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_data['features']:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = all_eq_data['metadata']['title']
fig = px.scatter_geo(lat = lats, lon = lons, size =mags, title=title, 
                    color = mags,
                    color_continuous_scale = 'Viridis',
                    labels= {'color': 'Magnitude'},
                    projection='natural earth',
                    hover_name=eq_titles
                     )
fig.show()
