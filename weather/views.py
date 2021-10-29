from django.shortcuts import render
import requests

# Create your views here.

def index(request):  
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=23f4b51c5db496500c933177029ad243'
    city = 'Las Vegas'

    r = requests.get(url.format(city)).json()
        

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],
        'temp_min': r['main']['temp_min'],
        'temp_max': r['main']['temp_max'],
        'description' : r['weather'][0]['description'],
        'icon' : r['weather'][0]['icon'],        

    }

    context = {'city_weather': city_weather}

    return render(request, 'weather/weather.html', context)
