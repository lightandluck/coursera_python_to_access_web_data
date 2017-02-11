# geo_json.py
''' Get geo_json from static resource '''
import urllib.request
import urllib.parse
import json

def geo_json():
    ''' Get geo_json '''
    service_url = 'http://python-data.dr-chuck.net/geojson?'

    while True:
        address = input('Enter location: ')
        if len(address) < 1:
            break

        url = service_url + urllib.parse.urlencode({
            'sensor': 'false',
            'address': address
        })
        print('Retrieving: ' + url)
        json_data = json.loads(urllib.request.urlopen(url).read())
        # print(json.dumps(json_data, indent=2))
        print(json_data['results'][0]['place_id'])

geo_json()







