import json
import requests
import csv
def meteo(city):
    api_key = "b8bdb7d52b20aa7c239f409d7f009840"
    # requete post
    url = "https://api.openweathermap.org/data/2.5/forecast?lang=fr&q=%s&appid=%s" % (city, api_key)
    x = requests.get(url)
    try:
        x = json.loads(x.text)
        x = x['list']
        i = 0
        tab=""
        while(i<40):
            y = x[i]
            main = y['main']
            date = y['dt_txt']
            temp = main['temp'] - 273.15
            temp = round(temp)
            temp_min = main['temp_min'] - 273.15
            temp_min = round(temp_min)
            temp_max = main['temp_max'] - 273.15
            temp_max = round(temp_max)
            tab= tab+"Ville: %s  \ntemperature : %s c\ntemperature min : %s c\ntemperature max : %s c\ndate : %s \n" % (
            city, temp, temp_min, temp_max,date)
            i = i + 1
        fichier = open("data.txt", "w+")
        fichier.write(tab)
        fichier.close()
    except:
        yolo = input('entre une nouvelle ville avec le bon nom cette fois ...')
        meteo(yolo)
yolo= input("Entrez la ville ")
meteo(yolo)