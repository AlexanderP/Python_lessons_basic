
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

import openweather
import sys

def print_help():
    print("--csv filename [<город>] - экспорт базы в формат csv")
    print("--json filename [<город>] - экспорт базы в формат json")
    print("--html filename [<город>] - экспорт базы в формат html")

db = openweather.Sqlite()

key_list = ["--csv","--json","--html"]

try:
    filename_name = sys.argv[2]
except IndexError:
    filename_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

try:
    city = sys.argv[3]
except IndexError:
    city = ""


if key:
    if key in key_list and not filename_name is None:
        db.import_file(filename_name, city)
    elif key == 'help':
        print_help()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")