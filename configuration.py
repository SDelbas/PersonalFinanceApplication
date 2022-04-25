import json
import os
from os import path


class Configuration:
    def __init__(self):
        self.fileName = 'config.json'
        self.firstRun = True
        self.fileLocation = None
        self.location_current_csv = None
        self.location_current_master = None
        self.location_old_csv = None
        self.location_old_master = None

        if path.exists('config.json'):
            self.read()

    def write(self):
        """
        Write the local config file

        :return: None
        """
        with open(self.fileName, 'w') as jsonfile:
            json.dump(self.__dict__, jsonfile)
            print('Write successful')
        return

    def read(self):
        """
        Read the local JSON file

        :return: None
        """
        with open(self.fileName) as infile:
            config_dict = json.load(infile)
            for k, v in config_dict.items():
                setattr(self, k, v)
        return

    def set_folders(self, location):
        self.fileLocation = os.path.normpath(location)
        self.location_current_csv = os.path.join(location, 'current\\csv')
        self.location_current_master = os.path.join(location, 'current\\master')
        self.location_old_csv = os.path.join(location, 'old\\csv')
        self.location_old_master = os.path.join(location, 'old\\master')
        self.write()
