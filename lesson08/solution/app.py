from libs.city import City
from libs.weather import Weather
from libs.database import Database

import os
import re
from settings import *

# Download cities
print("Initializing weather app ... please wait")
City.download_archive(ARCHIVE_URL, EXPORT_DIR)
cities = City.get_list(EXPORT_DIR)

# Init database
db = Database(os.path.join(EXPORT_DIR, 'storage.db'))

# Ask city/country name from user
input_name = input("Type city/country name to find: ")

# Try to find city by name with regex
pattern = re.compile(r'('+input_name+')+', flags=re.IGNORECASE)
founded_items = list(filter(lambda item: pattern.match(item.name), cities))

print("\nCities founded: ")
for x in founded_items:
    print(x)

# Get city ID
city_id = int(input('\nType city id: '))

# Try to get JSON weather
city = Weather(API_KEY, city_id)

# Try to save/update weather in DB
db.save_weather(city)
