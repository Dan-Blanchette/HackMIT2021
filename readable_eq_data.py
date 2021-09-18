import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'significant.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, longi, lats, = [] ,[], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    longi.append(lon)
    lats.append(lat)
# map the earthquakes
data = [Scattergeo(lon=longi, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='global_earthquakes.html')
#print(mags[:10])
#print(longi[:5])
#print(lats[:5])
