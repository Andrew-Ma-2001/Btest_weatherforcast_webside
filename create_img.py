import cv2
import numpy as np
import pypinyin
from find import Little_Pony_Weather
from PIL import Image


def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


def alpha2white_opencv2(img):
    sp = img.shape
    width = sp[0]
    height = sp[1]
    for yh in range(height):
        for xw in range(width):
            color_d = img[xw, yh]
            if (color_d[3] == 0):
                img[xw, yh] = [255, 255, 255, 255]
    return img


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    sheet = np.zeros((168, 250, 4), np.uint8)
    sheet.fill(255)
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        print(xy)
        cv2.circle(sheet, (x, y), 1, (255, 0, 0), thickness=-1)
        cv2.putText(sheet, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 0), thickness=1)
        cv2.imshow("image", sheet)


def create_weather_img(model):
    # Create White Image
    sheet = np.zeros((168, 250, 4), np.uint8)
    sheet.fill(255)
    # Get Data From Model
    city_chinese, city_tem, icon, weather_word, air_dic = model.return_data()
    # Preparing Data
    location = pinyin(city_chinese[:-1]).title()
    air_level = air_dic['level']
    air_number = air_dic['aqi']
    path = 'weather_icon/weather-icon-S2/64'
    weather_icon = path + '/' + str(icon) + '.png'
    weather_img = cv2.imread(weather_icon, -1)
    weather_img = alpha2white_opencv2(weather_img)
    sheet[30:94, 148:212] = weather_img
    # Showing On Image
    cv2.putText(sheet, location, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(sheet, str(city_tem) + 'C', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)
    cv2.putText(sheet, f'Air Quality Level:{air_level}', (30, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    cv2.putText(sheet, f'Air Pollution Number:{air_number}', (30, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
    sheet = cv2.resize(sheet, (500, 336))
    sheet = cv2.cvtColor(sheet,cv2.COLOR_RGBA2BGR)
    return sheet


if __name__ == '__main__':
    model = Little_Pony_Weather()
    img = create_weather_img(model)
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
