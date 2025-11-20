import pandas as pd
from pyproj import Transformer
import folium

colour_palette = ['#448AFF', '#1565C0', '#009688', '#8BC34A', '#FFC107', '#FF9800', '#F44336', '#AD1457']

def add_legend(map_object, title, items_dict, position='bottomleft'):
    pos_css = {
        'bottomleft': 'bottom: 50px; left: 50px;',
        'bottomright': 'bottom: 50px; right: 50px;',
        'topleft': 'top: 50px; left: 50px;',
        'topright': 'top: 50px; right: 50px;'
    }[position]

    legend_html = f'''
    <div style="
        position: fixed; 
        {pos_css}
        width: 250px; 
        background-color: white; 
        border:2px solid grey; 
        z-index:9999; 
        font-size:14px;
        padding: 10px;
        border-radius: 10px;
    ">
    <b>{title}</b><br>
    '''
    for label, color in items_dict.items():
        legend_html += f'<span style="color:{color};">&#9679;</span> {label}<br>'
    legend_html += '</div>'

    map_object.get_root().html.add_child(folium.Element(legend_html))

# Load data
gias = pd.read_csv("gias.csv", encoding="latin1", low_memory=False)
additional_locations = pd.read_csv("additional_locations.csv")

# Basic cleaning
gias = gias[['EstablishmentName', 'Postcode', 'Easting', 'Northing', 'PhaseOfEducation (code)', 'PhaseOfEducation (name)']].dropna()

# Create a transformer from British National Grid (EPSG:27700) to WGS84 (EPSG:4326)
transformer = Transformer.from_crs("epsg:27700", "epsg:4326", always_xy=True)

# Apply the transformation
gias["Longitude"], gias["Latitude"] = transformer.transform(
    gias["Easting"].values, gias["Northing"].values
)

m = folium.Map(location=[53.55, -2.87], zoom_start=10)

legend_items = {}

for _, row in gias.iterrows():
    phase_code = row['PhaseOfEducation (code)']
    phase_name = row['PhaseOfEducation (name)']

    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=2,
        popup=row['EstablishmentName'],
        color=colour_palette[phase_code],
        fill=True,
    ).add_to(m)

    legend_items[phase_name] = colour_palette[phase_code]

for _, row in additional_locations.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=row["description"],
        icon=folium.Icon(color="red", icon="home")
    ).add_to(m)

add_legend(m, "School Types", legend_items)

m.save("schools_map_c.html")
print("Map created: schools_map_c.html")
