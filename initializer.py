# The purpose of this function is to initialize the Dash application and read/write relevant configuration data in JSON
import json

config = {
    'first_run': True
}


def initializer():
    if config['first_run'] in [True, None]:
        print('Program setup initiated')

        config['first_run'] = False

        # Write to JSON
        with open ('config.json','w') as jsonfile:
            json.dump(config, jsonfile)
            print('Write successful')

    return


def installation():
    return
