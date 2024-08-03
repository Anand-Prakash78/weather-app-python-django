import requests
from django.shortcuts import render
from django.conf import settings


def get_weather(request):
    if request.method == 'POST':
        city="Bareilly"
        city = request.POST.get('city')
        api_key = 'eae8c0d8a585a09a2b0c275b8fdf463b'  # Replace with your actual API key
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

        response = requests.get(api_url)
        weather_data = response.json()

        if weather_data.get('cod') != 200:
            context = {'error': weather_data.get('message')}
        else:
            context = {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'pressure':weather_data['main']['pressure'],
                'humidity':weather_data['main']['humidity'] ,
                'windspeed':weather_data['wind']['speed'],
                'description': weather_data['weather'][0]['description'],
                
                'icon': weather_data['weather'][0]['icon'],
            }
        return render(request, 'index.html', context)
    return render(request, 'index.html')
