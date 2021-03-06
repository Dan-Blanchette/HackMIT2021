# Daniel Blanchette
# HackMIT 2021 Project
# Resources used: Crash Course Python 2nd editon by Eric Matthes (Chapter 16 Downloading Data)
# 9/18/2021

# This program interprets geoJSON files and creates a scatterplot model on a mercator projection map.
# The data is output is converted into an offline HTML5 file format

import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/significant30.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

# plot point entry formatting
mags, longi, lats, hover_texts = [] ,[], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    longi.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': longi, 
    'lat': lats,
    'text': hover_texts,
    'marker': { 
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename='html/global_earthquakes30.html')
