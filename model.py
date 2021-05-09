import json
import requests



def readFile():
    with open('_city.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)
    return data


def getCode(data, city_name):
    result = [item['city_code'] for item in data if item['city_name'] == str(city_name)]
    if result:
        city_code = result[0]
    else:
        city_code = None
    return city_code


def getWeather(city_code):
    url = 'http://t.weather.sojson.com/api/weather/city/' + str(city_code)
    response = requests.get(url)
    content = response.json()
    if content['message'] == 'Success !':
        result = content['data']
    else:
        result = None
    return result


def showResult(result, day):
    for i in range(day):
        print('----------' + result['forecast'][i]['ymd'] + ' ' + result['forecast'][i]['week'] + '----------')
        print('天气类型：' + result['forecast'][i]['type'])
        print('最高温度：' + result['forecast'][i]['high'])
        print('最低温度：' + result['forecast'][i]['low'])
        print('风力：' + result['forecast'][i]['fl'])
        print('风向：' + result['forecast'][i]['fx'])
        print('日出时间：' + result['forecast'][i]['sunrise'])
        print('日落时间：' + result['forecast'][i]['sunset'])
        print('温馨提示：' + result['forecast'][i]['notice'])


if __name__ == '__main__':
    data = readFile()
    while True:
        print('---------------查询参数---------------')
        city_name = input('城市名称：')
        city_code = getCode(data, city_name)
        if not city_code:
            print('输入错误，请重新输入')
            continue
        result = getWeather(city_code)
        if not result:
            print('查询错误，请重新输入')
            continue
        day = input('查询天数：')
        if not day.isdigit():
            print('查询天数必须是数字，请重新输入')
            continue
        if not 0 <= int(day) <= 15:
            print('查询天数必须小于十五天，请重新输入')
            continue
        showResult(result, int(day))
