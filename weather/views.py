from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):  
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=23f4b51c5db496500c933177029ad243'    

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()      

    form = CityForm()        

    cities = City.objects.all()

    data = []

    for city in cities:

        r = requests.get(url.format(city)).json()            

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'temp_min': r['main']['temp_min'],
            'temp_max': r['main']['temp_max'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],       

        }

        data.append(city_weather)

    context = {'data': data, 'form':form}

    return render(request, 'weather/weather.html', context)
