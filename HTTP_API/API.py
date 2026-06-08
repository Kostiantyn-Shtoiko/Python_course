# import requests
#
# url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02"
# response = requests.get(url, headers={'Accept': 'application/json'}, params={'format': 'geojson',
#                                                                              'starttime':'2014-01-01',
#                                                                             'endtime' : '2014-01-02'})
# # print(response.text)
# # print(response.json())
#
# data = response.json()
# print(data['features'][1]['properties']['place'])


# Homework

import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

starttime = input("Enter start date: ")
endtime = input("Enter end date: ")
latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")
maxradius = input("Enter max radius: ")
minmagnitude = input("Enter minmagnitude: ")

params = {
    'format': 'geojson',
    'starttime': starttime,
    'endtime': endtime,
    'latitude': latitude,
    'longitude': longitude,
    'maxradius': maxradius,
   'minmagnitude': minmagnitude
}

response = requests.get(url, params=params)

data = response.json()
earthquakes = data['features']

earthquake = earthquakes[0]

for i, item in enumerate(earthquakes):
    print(i + 1, item["properties"]["place"], item["properties"]["time"])






