# The purpose of this function is to initialize the Dash application and read/write relevant configuration data in JSON
import json
from os import path


class Configuration:
    def __init__(self):
        self.fileName = 'config.json'
        self.firstRun = True

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

    def check_status(self):
        if self.firstRun in [True, None]:
            print('Program setup initiated')

            self.firstRun = False

            self.write()
        return


