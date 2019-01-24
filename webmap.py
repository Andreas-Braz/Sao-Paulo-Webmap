import folium
import pandas

data = pandas.read_csv("SP-TP.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
nam = list(data["NAME"])
add = list(data["ADDRESS"])

html = """
Tourist Place:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Address: %s
"""
def color(nm):
    nmsplit = nm.split(" ")
    if nmsplit[0] == "Parque":
        return "green"
    elif nmsplit[0] == "Museu":
        return "red"
    else:
        return "blue"


map = folium.Map(location=[-23.5305,-46.6700],
                 zoom_start=10,
                 tiles="Stamen Terrain")

#zip function to iterate 2 lists at the same time.

for lt, ln, nm, ad in zip(lat, lon, nam, add):
    iframe = folium.IFrame(html=html % (nm, nm, ad), width=200, height=100)
    folium.Marker(location = [lt,ln],
                  popup=folium.Popup(iframe),
                  #popup = str(nm) + " / " + str(ad),
                  icon = folium.Icon(color = color(nm),
                  icon = "info-sign")).add_to(map)

map.save("Map_html_popup_advanced.html")