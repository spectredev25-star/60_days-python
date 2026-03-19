import requests
import sys

weather_icons = {
    'rain':'🌧',
    'clear':'☀',
    'clouds':'☁',
    'snow':'❄',
    'thunderstorm':'⛈'
}
def get_weather(city,api_key):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    params = {
    'q':city,
    'appid':api_key,
    'units':'metric'
}
    try:
        response = requests.get(BASE_URL,params=params)
        response.raise_for_status()
        data = response.json()
        temperature = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        weather = data['weather'][0]['main'].lower()
        weather_icon = weather_icons.get(weather,'😀')
        
        print(f'TEMPERATURE IN {city} IS {temperature}C')
        print(f'DESCRIPTION: {description}')
        print(f'HUMIDITY: {humidity}%')
        print(f'WIND SPEED: {wind_speed}m/s')
        print(f'IT IS {weather.upper()} TODAY {weather_icon}.')
    
    except requests.exceptions.HTTPError:
        print('CITY NOT FOUND OR INVALID API KEY')
    except Exception as e:
        print(f'AN ERROR OCCURED: {e}')

    
    

if __name__ == '__main__':
    API_KEY = "28de681efac5b4b5f62b2a82a0163875"
    user_city = input('ENTER CITY NAME: ')
    get_weather(user_city,API_KEY)
