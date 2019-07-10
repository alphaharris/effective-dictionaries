"""
Remember, remember, the 5th normal member...
"""

members = dir(dict)
[m for m in members if not m.startswith('__')][4]

"""
Defining and iterating
"""
my_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
}

# .items() .keys() .values()
for k, v in my_dict.items():
    print('key: ', k)
    print('value: ', v)

# .keys() is nice for readability

"""
Handling JSON
"""
tt_key = 'bwsB1D5UpFjbZn1EIu6bXM4WvsGr0uAq'

import requests

output = '.json?'
endpoint = 'https://api.tomtom.com/search/2/batch' + output
address = '701 Brazos St, Austin, TX 78701'

# https://api.tomtom.com/search/2/batch.json?key=*****
headers = {'Content-Type': 'application/json'}
data = {
    "batchItems": [
        # {"query": "/geocode/ " + address + ".json"} for address in address_dicts.values()]
        {"query": "/geocode/ " + address + ".json"}]
}
params = {
    'key': tt_key,
    # limit geography (optional)
    'countrySet': 'US',
    'topLeft': '30.506667,  -97.967834',
    'bttmRight': '30.022733, -97.443237',
}
r = requests.post(endpoint, params=params, headers=headers, json=data)
print(r.url)
response = r.json()
type(response)
# <class 'dict'>

# Okay, we have a dict! Now what?
from pprint import pprint

pprint(response)

# Usually 8 or 10 responses, sorted by accuracy
results = response['batchItems'][0]['response']['results']

first_result = {'type': 'Point Address', 'id': 'US/PAD/p0/3077466', 'score': 11.9658,
                'address': {'streetNumber': '701',
                            'streetName': 'Brazos Street', 'municipalitySubdivision': 'Austin, Downtown',
                            'municipality': 'Austin', 'countrySecondarySubdivision': 'Travis',
                            'countryTertiarySubdivision': 'Austin',
                            'countrySubdivision': 'TX', 'postalCode': '78701', 'extendedPostalCode': '787012262',
                            'countryCode': 'US',
                            'country': 'United States', 'countryCodeISO3': 'USA',
                            'freeformAddress': '701 Brazos Street, Austin, TX 78701', 'localName': 'Austin',
                            'countrySubdivisionName': 'Texas'}, 'position': {'lat': 30.26895, 'lon': -97.74042},
                'viewport': {'topLeftPoint': {'lat': 30.26985, 'lon': -97.74146},
                             'btmRightPoint': {'lat': 30.26805, 'lon': -97.73938}},
                'entryPoints': [{'type': 'main', 'position': {'lat': 30.2691, 'lon': -97.74095}}]}

import pandas as pd

# Pandas will do it's best to store this data
row = pd.Series(first_result)
row

"""
Comprehension for creating a row
"""
# What we want
row = {
    'type': '...',
    'streetName': '...',
    'lat': '...',
    'lon': '...',
}

# How we get it

table = {results.index(r): {
    'type': r['type'],
    'streetName': r['address']['streetName'],
    'lat': r['position']['lat'],
    'lon': r['position']['lon'],
} for r in results}

pprint(table)


"""
{0: {'lat': 30.26895,
     'lon': -97.74042,
     'streetName': 'Brazos Street',
     'type': 'Point Address'},
 1: {'lat': 30.27094,
     'lon': -97.74026,
     'streetName': 'Brazos Street',
     'type': 'Street'},
 2: {'lat': 30.27649,
     'lon': -97.73821,
     'streetName': 'Brazos Street & East 15th Street',
     'type': 'Cross Street'},
 3: {'lat': 30.27236,
     'lon': -97.73974,
     'streetName': 'Brazos Street & East 11th Street',
     'type': 'Cross Street'},

"""

"""
Readability - Dash + Mapbox
"""


def bigfoot_map(sightings):
    # groupby returns a dictionary mapping the values of the first field
    # 'classification' onto a list of record dictionaries with that
    # classification value.
    classifications = groupby('classification', sightings)
    return {
        "data": [
            {"type": "scattermapbox",
             "lat": listpluck("latitude", class_sightings),
             "lon": listpluck("longitude", class_sightings),
             "text": listpluck("title", class_sightings),
             "mode": "markers",
             "name": classification,
             "marker": {
                 "size": 3,
                 "opacity": 1.0}
             }
            for classification, class_sightings in classifications.items()
        ]}


dict(
    type="scattermapbox",
    lat=listpluck("latitude", class_sightings),
    lon=listpluck("longitude", class_sightings),
    text=listpluck("title", class_sightings),
    mode="markers",
    name=classification,
    marker={
        size: 3,
        opacity: 1.0}
)

"""
Comprehensions and Enhancements
"""

# list comp

# dict comp

# defaultdict

# OrderedDict

"""
Interacting with Pandas
"""
