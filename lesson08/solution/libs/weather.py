import urllib3
import json
from datetime import date

class Weather (object):
    city_id: int
    city_name: str
    date: str
    temperature: int
    weather_id: int
    weather_icon: str

    def __init__(self, api_key: str, city_id: int):
        http = urllib3.PoolManager()
        request_url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&appid={api_key}'

        request = http.request('GET', request_url)
        response = json.loads(request.data)

        self.city_id = city_id
        self.city_name = response['name']
        self.date = date.today().strftime('%d-%m-%Y')
        self.temperature = int(response['main']['temp'])
        self.weather_id = int(response['weather'][0]['id'])
        self.weather_icon = response['weather'][0]['icon']

    def html_output(self):
        return f'''
            <h1>City: {self.city_name}</h1>
            <img src="http://openweathermap.org/img/w/{self.weather_icon}.png">
            <h2>Temperature: {self.temperature}˚</h2>
        '''
