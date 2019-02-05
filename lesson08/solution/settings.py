import os

# Settings
API_KEY = '88b34798998475dc9b8e896b74af6df8'
ARCHIVE_URL = 'http://bulk.openweathermap.org/sample/city.list.json.gz'

EXPORT_DIR = os.path.join(
    os.path.dirname(__file__),
    'assets'
)
