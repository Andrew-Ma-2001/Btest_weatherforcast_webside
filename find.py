import requests


WEATHER_KEY = '75d7f085da6e4c5186579e67a1320379'
LOCATION_KEY = 'a099318042c608f01b656720ef58ec1e'


def get_location():
    url = 'https://restapi.amap.com/v3/ip?' + 'key=' + LOCATION_KEY
    strhtml = requests.get(url)

    data = strhtml.json()
    province, city = data['province'], data['city']
    dic = {'province':province, 'city':city}
    return dic

def get_city(location):
    url = 'https://geoapi.qweather.com/v2/city/lookup?' + 'location=' + str(location) + '&key=' + WEATHER_KEY
    strhtml = requests.get(url)
    data = strhtml.json()
    name, id = data['location'][0]['name'], data['location'][0]['id']
    dic = {'name':name,'id':id}
    return dic

def get_city_weather(id):
    url = 'https://devapi.qweather.com/v7/weather/now?' +  'key=' + WEATHER_KEY + '&location=' + str(id)
    strhtml = requests.get(url)
    data = strhtml.json()
    tem, icon, word = data['now']['temp'], data['now']['icon'], data['now']['text']
    dic = {'tem':tem, 'icon':icon,'word':word}
    return dic

def get_city_air(id):
    url = 'https://devapi.qweather.com/v7/air/now?' + 'key=' + WEATHER_KEY + '&location=' + str(id)
    strhtml = requests.get(url)
    data = strhtml.json()
    air = data['now']
    return air



location_dic = get_location()
city_dic = get_city(location_dic['city'])
city_weather_dic = get_city_weather(city_dic['id'])
print(city_dic,city_weather_dic)
air = get_city_air(city_dic['id'])
print(air)



