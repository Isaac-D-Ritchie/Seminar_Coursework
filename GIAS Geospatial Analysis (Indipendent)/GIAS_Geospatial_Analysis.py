"""
In this code i will be taking information from the public UK GIAS (Get Information About Schools) databse. 
The GIAS database (.CSV) contains information about different all schools within englnd and wales, and some connected schools in scotland
I will be pulling from This databse to analyise different information within it and generate a interactive visualisation map.
"""
import pandas as pd

#Load GIAS database.
gias = pd.read_csv("gias.csv", encoding="latin1", low_memory=False)
#Cleans up data formating.
gias = gias[["EstablishmentName","Postcode","Easting","Northing"]].dropna()

#Test print header or the database
print(gias.head())

#Imports a feature inside pyproj that converts the 'lat' and 'lon' to gps.
from pyproj import Transformer

#Converts uk format (27700) to glabal format (4326) for the next module to use.
transformer = Transformer.from_crs("epsg:27700", "epsg:4326")
gias["Longitude"], gias["Latitude"] = transformer.transform(gias["Easting"].values, gias["Northing"].values)
#Test transformation
#print(gias[["Easting", "Northing", "Longitude", "Latitude"]].head())

#Imports module to create a html map
import folium

#setting m as a map of the types co-ordinates (roughly the uk) aswell as how zoomed in.
m = folium.Map(location=[53.55, -2.87], zoom_start=6)

for _, row in gias.iterrows():
    #Creates small circles on the map.
    folium.CircleMarker(
        location=[row["Longitude"], row["Latitude"]], #Location of school.
        radius=2, #Size of marker
        popup=row['EstablishmentName'], #Creates a clickable popup.
        color='blue', fill=True, #Marker colours and fill.
    ).add_to(m) #Adds marker to the map made previously.

#Creates a html file of the map.
m.save("schools_map.html")
#Prints file if code does not error, therefore the map has been sucesfully created.
print("Map created: schools_map.html")

