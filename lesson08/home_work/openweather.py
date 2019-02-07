"""
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=583509&appid=f0dafe554ae9c96c0a1f2a8d2aca14ef

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""
import gzip
import json
import os
import os.path
import re
import sqlite3
import time
import requests
import csv


class ApiKey(object):

    def __init__(self, app_id='app.id'):
        with open(app_id, 'r') as id_file:
            self.api_key = id_file.read().strip()

    def __str__(self):
        return self.api_key

    def __repr__(self):
        return self.__str__()


class City(object):
    name: str
    country: str
    id: int
    json_city: list
    iso_dict: dict

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)

    @classmethod
    def get_city(cls, force=False):
        url = [
            'http://bulk.openweathermap.org/sample',
            'city.list.json.gz'
        ]
        if force or not os.path.exists(os.path.join(os.getcwd(), 'db', url[1])):
            json_get = requests.get('/'.join(url))
            if not os.path.exists(os.path.join(os.getcwd(), 'db')):
                os.mkdir('db')
            with open(os.path.join(os.getcwd(), 'db', url[1]),
                      'wb') as tmp_file:
                tmp_file.write(json_get.content)
        cls.json_city = json.loads(
            gzip.open(os.path.join(os.getcwd(), 'db', url[1])).read())
        with open(os.path.join(os.getcwd(), 'db', 'iso.json')) as json_iso:
            cls.iso_dict = json.loads(json_iso.read())

    def __str__(self):
        if self.country == '' or not self.iso_dict.get(self.country):
            country = 'н/д'
        else:
            country = f'{self.iso_dict[self.country]}'

        return (f'Название города: {self.name}, '
                f'Страна: {country}, '
                f'Код страны: {self.country}, '
                f'Идентификатор: {self.id}.')

    def __repr__(self):
        return self.__str__()

    @classmethod
    def get_list(cls):
        city = []
        for _city in cls.json_city:
            city.append(City(_city))
        return city


class OpenWeatherMap(object):

    def __init__(self):
        self.api_key = ApiKey()
        City.get_city()
        self.db = Sqlite()

    def main(self):
        answer = input(
            'Введите название страны, название города или код страны: ')
        pattern = re.compile(".*(" + answer + ").*")
        list_city = list(
            filter(lambda x: re.search(pattern, str(x)), City.get_list()))
        if len(list_city) == 0:
            print('Совпадений не найденно')
            return
        for _city in list_city:
            print(_city)
        try:
            answer = [int(x) for x in
                      input('Введите идентификаторы[через пробел]: ').split()]
        except ValueError:
            print("Ошибка. Необходимо ввести числовое значение.")
        for _city in self.weather(answer):
            weather_city = Weather(_city)
            self.db.add_weather(weather_city)
            print(weather_city)

    def weather(self, id):
        args = {
            "units": "metric",
            "appid": self.api_key,
        }
        if len(id) == 1:
            url = "http://api.openweathermap.org/data/2.5/weather"
            args["id"] = str(id[0]),
            json_get = requests.get(url, params=args)
            return [json.loads(json_get.text)]
        else:
            url = "http://api.openweathermap.org/data/2.5/group"
            args["id"] = ",".join(list(map(str, id))),
            json_get = requests.get(url, params=args)
            return json.loads(json_get.text)['list']


class Weather(object):
    def __init__(self, dictionary):
        self.name = dictionary["name"]
        self.id = dictionary["id"]
        self.temp = dictionary["main"]["temp"]
        self.pressure = dictionary["main"]["pressure"]
        self.humidity = dictionary["main"]["humidity"]
        self.weather_id = dictionary["weather"][0]["id"]
        self.weather_main = dictionary["weather"][0]["main"]
        self.weather_icon = dictionary["weather"][0]["icon"]

    def __str__(self):
        return (f'В городе {self.name} '
                f'температура {self.temp} С° '
                f'погода {self.weather_main}')


class Sqlite(object):
    db_path = os.path.join(os.getcwd(), 'db', 'db.sqlite')

    def __init__(self):
        if not os.path.exists(self.db_path):
            self.sql = sqlite3.connect(self.db_path)
            self.sql.cursor()
            self.sql.execute("""CREATE TABLE weather
                              (id INTEGER PRIMARY KEY,
                                city VARCHAR(255),
                                data DATE,
                                temp INTEGER, 
                                weather_id INTEGER,
                                weather_icon VARCHAR(50))
                            """)
            self.sql.close()
        self.sql = sqlite3.connect(self.db_path)

    def add_weather(self, weather):
        self.sql.cursor()
        data = self.sql.execute(
            f"SELECT * FROM weather WHERE id={weather.id}").fetchall()
        date = time.strftime('%Y/%m/%d', time.localtime())
        if len(data) == 0:
            insert = f"""INSERT INTO weather
                    VALUES ('{weather.id}',
                    '{weather.name}',
                    '{date}',
                    '{weather.temp}',
                    '{weather.weather_id}',
                    '{weather.weather_icon}')"""
            self.sql.execute(insert)
            self.sql.commit()
            self.sql.cursor().close()
        else:
            update = f"""
                    UPDATE weather 
                    SET data = '{date}',
                    temp = '{weather.temp}',
                    weather_id = '{weather.weather_id}',
                    weather_icon = '{weather.weather_icon}'
                    WHERE id = '{weather.id}'"""
            self.sql.execute(update)
            self.sql.commit()
            self.sql.cursor().close()

    def import_file(self, file: str, city=""):
        dict_title = [
            "id",
            "city",
            "data",
            "temp",
            "weather_id",
            "weather_icon"
        ]
        self.sql.cursor()
        if city == "":
            select = f"SELECT * FROM weather"
        else:
            select = f"SELECT * FROM weather WHERE city='{city}'"
        data = self.sql.execute(select).fetchall()
        self.sql.cursor().close()
        if len(data) == 0:
            if city == "":
                print(f'База данных не имеет значений')
                return
            else:
                print(f"В базе данных нет города {city}")
                return
        if file.endswith('.json'):
            json_list = []
            for _city in data:
                json_list.append(dict(zip(dict_title, _city)))
            with open(file, 'w') as json_file:
                json_write = json.dumps(json_list, indent=4, sort_keys=True)
                json_file.write(json_write)
        elif file.endswith('.csv'):
            with open(file, 'w') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(dict_title)
                for _city in data:
                    writer.writerow(_city)
        elif file.endswith('.html'):
            with open(file, 'w') as html_file:
                html = ("<!DOCTYPE html>\n"
                        "<html>\n"
                        "<head>\n"
                        "    <meta charset=\"utf-8\">\n"
                        "    <title>Прогноз погоды</title>\n"
                        "</head>\n"
                        "<body>\n")
                for _city in data:
                    dict_city = dict(zip(dict_title, _city))
                    html += (f"В городе {dict_city['city']} "
                             f"температура {dict_city['temp']} С° "
                             f"погода <img src=\"http://openweathermap.org/img/"
                             f"w/{dict_city['weather_icon']}.png\" alt=\"\">"
                             f"<br><hr><br>\n")
                html += "</body>\n</html>\n"
                html_file.writelines(html)
        else:
            print('Неверный формат файла.')


if __name__ == '__main__':
    weather = OpenWeatherMap()
    weather.main()
