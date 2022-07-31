from configuration import Configuration
import filemanager

configuration = Configuration()
filemanager.setup(configuration)
filemanager.identify_new_files()