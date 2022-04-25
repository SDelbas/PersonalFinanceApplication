import json
import os
from os import path


class Configuration:
    def __init__(self):
        self.fileName = 'config.json'
        self.firstRun = True
        self.location_folder = None
        self.location_current_csv = None
        self.location_current_master = None
        self.location_old_csv = None
        self.location_old_master = None

        if path.exists('config.json'):
            self.read()

    def write(self):
        """
        Write the local config file
        """
        with open(self.fileName, 'w') as jsonfile:
            json.dump(self.__dict__, jsonfile)
            print('Write successful')

    def read(self):
        """
        Read the local JSON file
        """
        with open(self.fileName) as infile:
            config_dict = json.load(infile)
            for k, v in config_dict.items():
                setattr(self, k, v)

    def set_folders(self, location):
        """
        Set the data storage folders and write the updated configuration file to JSON.

        :param location: Where should all data storage folders be placed
        """
        self.location_folder = os.path.normpath(location)
        self.location_current_csv = os.path.join(location, 'current\\csv')
        self.location_current_master = os.path.join(location, 'current\\master')
        self.location_old_csv = os.path.join(location, 'old\\csv')
        self.location_old_master = os.path.join(location, 'old\\master')
        self.write()

    def create_folders(self):
        for value in {value for key, value in self.__dict__.items() if 'location' in key}:
            if not os.path.exists(value):
                os.makedirs(value)

