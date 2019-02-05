import os
import gzip
import json
import urllib3

class City (object):
    id: int
    name: str
    country: str

    def __init__(self, json_dict: dict):
        self.id = int(json_dict['id'])
        self.name = json_dict['name']
        self.country = json_dict['country']

    def __str__(self):
        return f"ID #{self.id}, City: {self.name}, Country: {self.country}"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def download_archive(url: str, destination_folder: str):
        archive_file = os.path.join(destination_folder, 'cities.gz')
        json_file = os.path.join(destination_folder, 'cities.json')

        if not os.path.exists(archive_file):
            print("Downloading cities archive from OpenWeather ...")

            http = urllib3.PoolManager()
            request_content = http.request('GET', url, preload_content=False)

            with open(archive_file, 'wb') as gzip_file:
                for part in request_content.stream(128):
                    gzip_file.write(part)

            request_content.release_conn()
        
        decompressed_content = gzip.open(archive_file).read()

        with open(json_file, 'wb') as json_output:
            json_output.write(decompressed_content)

    @staticmethod
    def get_list(export_dir: str):
        new_cities = []

        with open(os.path.join(export_dir, 'cities.json')) as json_file:
            json_data = json.load(json_file)

            for item in json_data:
                city = City(item)
                new_cities.append(city)

        return new_cities
