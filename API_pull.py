# python3

import requests
import json

# use the overpass API to obtain a json package from OSM

area_dict = {
    'Germany': '\"ISO3166-1\"=\"DE\"',
}



def OSM_pull():
    overpass_url = 'http://overpass-api.de/api/interpreter'
    overpass_query = """
    [out:json];
    area["ISO3166-1"="DE"][admin_level=2];
    (node["amenity"="biergarten"](area);
     way["amenity"="buergarten"](area);
     rel["amenity"=biergarten"](area);
    );
    out center
    """
    return requests.get(overpass_url, params={'data': overpass_query}).json()
    # response = requests.get(overpass_url, params={'data': overpass_query})
    # data = response.json()

# Use the json package to read the json file
data = OSM_pull()

## returns error: JSONDecodeError
## expecting value line 1 column 1 (char 0)