import requests

def extras(request):

    key = '97a718f8f6ef703241dbb3b5c06afff0'
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Baku&appid={key}&units=metric'
    api_data = requests.get(url.format()).json()

    weather_info = {
        'city': "Baku",
        'weather': api_data ['main']['temp'],
        'description': api_data ['weather'][0]['description'],
        'icon': api_data ['weather'][0]['icon'] ,
    }

    return {'weather': weather_info}