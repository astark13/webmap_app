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

fg = folium.FeatureGroup(name="My Map") # creates a group of features(e.g. markers, polygons, etc) that cand be added to the base map

for lt, ln, el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(el)+"m", 
    fill_color=color_producer(el), color='grey', fill_opacity=0.7))  # adds a point-layer containing markers with a location, message/popup, and color

# adds a polygon-layer that shows borders(areas) and based on data regarding population from the json assigns a color to each country
fg.add_child(folium.GeoJson(open("world.json",encoding = "utf-8-sig").read(), style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)

map.save("Map1.html")
