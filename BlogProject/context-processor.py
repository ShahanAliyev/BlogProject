import requests
import os

def extras(request):

    key = os.environ.get('key')
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Baku&appid={key}&units=metric'
    api_data = requests.get(url.format()).json()

    weather_info = {
        'city': "Baku",
        'weather': api_data ['main']['temp'],
        'description': api_data ['weather'][0]['description'],
        'icon': api_data ['weather'][0]['icon'] ,
    }

    return {'weather': weather_info}
