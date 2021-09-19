# Dan Blanchette
# Resources: Python Crash Course by: Eric Matthes
#This program will sort a geoJson file to better evaluate its meta data.
import json

# sort geoJSON file
filename = 'data/significant7.json'
with open(filename) as f:
    all_quake_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_quake_data, f, indent=4)