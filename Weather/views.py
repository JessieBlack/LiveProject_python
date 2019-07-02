from django.shortcuts import render
import requests
from .models import City
import json
import urllib

def index(request):
    url = 'http://openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=bf357a3c897f482670e76847febb1cb5'
    end_point = ""
    #if the request from the user is a city and not blank->get the location, weather, country, temperature, and wind speed
    if request.method == 'POST':
        CityName = request.POST.get('City_Name', None)
        print(CityName)
        end_point = url.format(CityName)
        print(end_point)
        r = requests.get(end_point).text
        cityinput = json.loads(r)
        city_weather = {
            'location': cityinput['name'],
            'country': cityinput['sys']['country'],
            'weather': cityinput['weather'][0]['description'],
            'temperature': cityinput['main']['temp'],
            'wind_speed': cityinput['wind']['speed'], 
        }
        # print(cityinput['name'])
        # print(cityinput['sys']['country'])
        # print(cityinput['weather'][0]['description'])
        # print(cityinput['main']['temp'])        
        # print(cityinput['wind']['speed'])
        # print(r)

        #renders request to server and displays onto browser screen at weather/weather.html
        return render(request, 'weather/weather.html', {'city_weather': city_weather})
    else:
        return render(request, 'weather/weather.html')

# def index(request):
#     url = 'http://openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=bf357a3c897f482670e76847febb1cb5'
#     end_point = ""
#     # res = evalInput(request)
#     if request.method == 'POST': #and res != False :
#         CityName = request.POST.get('City_Name', None)
#         #j = json.loads(urllib.request.urlopen(url).read())
#         #weather = {
#                 #'main' : j["temp_min"], {"temp_max"], ["humidity"],
               
#             #}
#         print(CityName)
#         end_point = url.format(CityName)
#         print(end_point)
#         r = requests.get(end_point).text
#         print(r)
#     return render(request, 'weather/weather.html')

# def code(request):
#     url = 'http://api.openweathermap.org/data/2.5/forecast?zip={}&units=imperial&appid=bf357a3c897f482670e76847febb1cb5'
#     end_point = ""
#     if request.method == 'POST':
#         Zip_Code = request.POST.get('ZipCode', None)
#         print(Zip_Code)
#         end_point = url.format(Zip_Code)
#         print(end_point)
#         r = requests.get(end_point).text
#         print(r)
#     return render(request, 'weather/weather.html')

# def evalInput(request):
#     city = request.POST.get('City_Name', None)
#     zip = request.POST.get('ZipCode', None)

#     if not city:
#         code(request)
#         return False
#     elif not zip:
#         return True

