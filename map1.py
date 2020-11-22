import folium, pandas
data=pandas.read_csv("Volcanoes.txt") # creates dataframe 
lat=list(data["LAT"])                 # turns dataframe column into list
lon=list(data["LON"])
name=list(data["NAME"])

map = folium.Map(location=[48.77,-121.81],zoom_start=10, tiles="Stamen Terrain") # creates a map with a base location

fg = folium.FeatureGroup(name="My Map") # creates a group of features(e.g. markers, polygons, etc) that cand be added to the base map

for lt, ln, na in zip(lat,lon,name):
    fg.add_child(folium.Marker(location=[lt,ln], popup=(na), icon=folium.Icon(color='green')))  # adds a marker with a location, message/popup, and color
map.add_child(fg)

map.save("Map1.html")
