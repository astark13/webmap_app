import folium, pandas
data=pandas.read_csv("Volcanoes.txt") # creates dataframe 
lat=list(data["LAT"])                 # turns dataframe column into list
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<=elevation<=3000: 
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[48.77,-121.81],zoom_start=10, tiles="Stamen Terrain") # creates a map with a base location

fgv = folium.FeatureGroup(name="Volcanoes") # creates a feature group layer that contains markers for volcanoes

for lt, ln, el in zip(lat,lon,elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+"m", 
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))  # each marker is represented by a circle, showing the altitude and different colors based on the altitude

fgp = folium.FeatureGroup(name="Population") # creates a feature group layer that contains data about population

# the fgp layer shows borders(areas) and based on data regarding population from the json assigns a color to each country
fgp.add_child(folium.GeoJson(open("world.json",encoding = "utf-8-sig").read(), style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)                    # adds the fgv layer to the map
map.add_child(fgp)                    # adds the fgp layer to the map
map.add_child(folium.LayerControl())  # creates a button in the upper right corner allowing you to disable/enable layers

map.save("Map1.html")
