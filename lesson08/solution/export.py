""" OpenWeatherMap (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом openweather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из командной строки и получает на входе:
    export_openweather.py --csv filename [<город>]
    export_openweather.py --json filename [<город>]
    export_openweather.py --html filename [<город>]
    
При выгрузке в html можно по коду погоды (weather.id) подтянуть 
соответствующие картинки отсюда:  http://openweathermap.org/weather-conditions

Экспорт происходит в файл filename.

Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе -
выводится соответствующее сообщение.

"""

import csv
import json
import sys
import os

from libs.database import Database
from libs.weather import Weather
from settings import API_KEY, EXPORT_DIR

args = sys.argv[1:]

if len(args) < 2:
    print('Invalid args number')
    exit(1)
else:
    filetype = args[0][2:]
    filename = args[1]
    
    if filetype != 'csv' and filetype != 'json' and filetype != 'html':
        print('Invalid filetype')
        exit(1)

if len(args) == 3:
    city_name = args[2]
else:
    city_name = None


def export(format, file_name, cityname=None):
    db = Database(os.path.join(EXPORT_DIR, 'storage.db'))
    keys = ['city_id', 'city', 'date', 'temp', 'weather_id']

    if cityname:
        db.cursor.execute(f"select * from weather where city='{cityname}'")
        result = db.cursor.fetchone()
        if result:
            result = dict(zip(keys, result))
        else:
            print('City not found!')
            exit(1)
    else:
        db.cursor.execute(f'select * from weather')
        result = db.cursor.fetchall()
        result = [dict(zip(keys, item)) for item in result]

    if result:
        filename = os.path.join(EXPORT_DIR, file_name)
        
        if format == 'csv':
            filename += '.csv'
            with open(filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys)
                if isinstance(result, list):
                    writer.writerows(result)
                else:
                    writer.writerow(result)

        elif format == 'json':
            filename += '.json'
            with open(filename, 'w') as jsonfile:
                json.dump(result, jsonfile)

        elif format == 'html':
            filename += '.html'
            if isinstance(result, list):
                html_output = ''
                for item in result:
                    weather_item = Weather(API_KEY, item['city_id'])
                    html_output += weather_item.html_output()
                    pass
            else:
                weather_item = Weather(API_KEY, result['city_id'])
                html_output = weather_item.html_output()
            
            with open(filename, 'w') as htmlfile:
                htmlfile.write(html_output)
    else:
        print('City not found!')
        exit(1)


export(filetype, filename, city_name)
