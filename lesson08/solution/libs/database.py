import os
import sqlite3

class Database (object):
    filepath: str
    connection: None
    cursor: None

    def __init__(self, db_file: str):
        self.filepath = db_file

        if not os.path.exists(db_file):
            self.create_table()
        else:
            self.setup_connection()

    def setup_connection(self):
        self.connection = sqlite3.connect(self.filepath)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.setup_connection()

        query = '''
            CREATE TABLE `weather` (
                `id_city` INTEGER PRIMARY KEY,
                `city` VARCHAR(255),
                `date` DATE,
                `temperature` INTEGER,
                `id_weather` INTEGER
            )
        '''

        self.cursor.execute(query)
        self.connection.commit()

    def save_weather(self, weather_object):
        city_query = f'select * from weather where id_city={weather_object.city_id}'

        self.cursor.execute(city_query)
        q = self.cursor.fetchone()

        if q:
            sql = f'update weather set \
                date={weather_object.date}, \
                temperature={weather_object.temperature}, \
                id_weather={weather_object.weather_id} \
                where id_city={weather_object.city_id} \
            '
        else:
            sql = f'''
                insert into weather (id_city,city,date,temperature,id_weather)
                values ({weather_object.city_id},'{weather_object.city_name}','{weather_object.date}',{weather_object.temperature},{weather_object.weather_id})
            '''

        self.cursor.execute(sql)
        self.connection.commit()
        print('\nWeather was written into database!')
