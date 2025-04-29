import requests
from django.shortcuts import render

def get_weather(request):
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city')
        api = '611df418314538598fb93cf98b2e9f23'  
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'

        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error_message = "Invalid city name or API issue."
 

    return render(request, 'weather.html', {'weather': weather_data, 'error': error_message})