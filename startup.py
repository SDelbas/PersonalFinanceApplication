# The purpose of this function is to initialize the Dash application and read/write relevant configuration data in JSON
import json
from os import path

# Name of the JSON config file
filename = 'config.json'


#
def initialize():
    config = config_setup()
    print(config)
    return config


def config_setup():
    """
    Evaluate if config exists or not.
    If it exists, read and return the config dictionary.
    If it does not exist, create and return the config dictionary.
    """
    if not path.exists('config.json'):
        config = {
            'first_run': True
        }
    else:
        config = config_read()
    return config


# Write config file to JSON
def config_write(config_local):
    """
    Write the local config file

    :param config_local: Data to be stored in config file
    :return: None
    """
    with open(filename, 'w') as jsonfile:
        json.dump(config_local, jsonfile)
        print('Write successful')
    return


# Read config file from JSON
def config_read():
    """
    Read the local JSON file

    :return: config
    """
    with open(filename) as infile:
        config_local = json.load(infile)
    print('Read successful')
    return config_local


def check_status(config):
    if config['first_run'] in [True, None]:
        print('Program setup initiated')

        config['first_run'] = False

        config_write('config.json')
    return
