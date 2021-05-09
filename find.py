import requests

WEATHER_KEY = '75d7f085da6e4c5186579e67a1320379'
LOCATION_KEY = 'a099318042c608f01b656720ef58ec1e'


class Little_Pony_Weather():

    def __init__(self,WEATHER_KEY, LOCATION_KEY):
        self.weather_key = WEATHER_KEY
        self.location_key = LOCATION_KEY

    def get_location(self):
        url = 'https://restapi.amap.com/v3/ip?' + 'key=' + self.location_key
        strhtml = requests.get(url)
        data = strhtml.json()
        self.province, self.city = data['province'], data['city']


    def get_city(self):
        self.get_location()
        url = 'https://geoapi.qweather.com/v2/city/lookup?' + 'location=' + str(self.city) \
              + '&key=' + self.weather_key
        strhtml = requests.get(url)
        data = strhtml.json()
        self.city_name,self.city_id = data['location'][0]['name'], data['location'][0]['id']


    def get_city_weather(self):
        url = 'https://devapi.qweather.com/v7/weather/now?' + 'key=' + self.weather_key \
              + '&location=' + str(self.city_id)
        strhtml = requests.get(url)
        data = strhtml.json()
        self.city_tem, self.weather_icon, self.weather_word = data['now']['temp'], data['now']['icon'], data['now']['text']

    def get_city_air(self):
        url = 'https://devapi.qweather.com/v7/air/now?' + 'key=' \
              + self.weather_key + '&location=' + str(self.city_id)
        strhtml = requests.get(url)
        data = strhtml.json()
        self.air = data['now']

    def return_data(self):
        self.get_location()
        self.get_city()
        self.get_city_weather()
        self.get_city_air()
        return [self.city, self.city_tem, self.weather_icon, self.weather_word, self.air]


app = Little_Pony_Weather(WEATHER_KEY,LOCATION_KEY)
a = app.return_data()
print(a)

# def get_location():
#     url = 'https://restapi.amap.com/v3/ip?' + 'key=' + LOCATION_KEY
#     strhtml = requests.get(url)
#
#     data = strhtml.json()
#     province, city = data['province'], data['city']
#     dic = {'province':province, 'city':city}
#     return dic
#
# def get_city(location):
#     url = 'https://geoapi.qweather.com/v2/city/lookup?' + 'location=' + str(location) + '&key=' + WEATHER_KEY
#     strhtml = requests.get(url)
#     data = strhtml.json()
#     name, id = data['location'][0]['name'], data['location'][0]['id']
#     dic = {'name':name,'id':id}
#     return dic
#
# def get_city_weather(id):
#     url = 'https://devapi.qweather.com/v7/weather/now?' +  'key=' + WEATHER_KEY + '&location=' + str(id)
#     strhtml = requests.get(url)
#     data = strhtml.json()
#     tem, icon, word = data['now']['temp'], data['now']['icon'], data['now']['text']
#     dic = {'tem':tem, 'icon':icon,'word':word}
#     return dic
#
# def get_city_air(id):
#     url = 'https://devapi.qweather.com/v7/air/now?' + 'key=' + WEATHER_KEY + '&location=' + str(id)
#     strhtml = requests.get(url)
#     data = strhtml.json()
#     air = data['now']
#     return air

# location_dic = get_location()
# city_dic = get_city(location_dic['city'])
# city_weather_dic = get_city_weather(city_dic['id'])
# print(city_dic,city_weather_dic)
# air = get_city_air(city_dic['id'])
# print(air)
