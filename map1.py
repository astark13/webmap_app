import folium
map = folium.Map(location=[45.40,23.37],zoom_start=10, tiles="Stamen Terrain") # creates a map with a base location

fg = folium.FeatureGroup(name="My Map") # creates a group of features(e.g. markers, polygons, etc) that cand be added to the base map

for coordinates in [[45.33,23.12],[45.37,23.28]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I'm a marker", icon=folium.Icon(color='green')))  # adds a marker with a location, message/popup, and color
map.add_child(fg)

map.save("Map1.html")
