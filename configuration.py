import json
import os
from os import path
from tkinter import filedialog
from tkinter import messagebox


# ToDo Add observer changes; when making changes to the configuration object the result should be written to config.json

def designate_folder(message):
    """
    Prompts the user to select a folder where all necessary files will be saved.

    :return: Filepath of the selected folder.
    """
    if messagebox.askokcancel(title="Designate folder", message=message):
        return filedialog.askdirectory()

    else:
        exit()


def create_folder(basepath, foldername):
    """
    Creates a folder on a specified location with a specified name.

    :param basepath: Location where the folder is to be created.
    :param foldername: Name of the folder to be created.
    :return: Return the file path of the new folder.
    """
    folderpath = os.path.join(basepath, foldername)
    os.mkdir(folderpath)
    return folderpath


global folder_Main
global folder_BS
global folder_BS_New
global folder_BS_Old
global folder_BS_Processed


class Configuration:
    def __init__(self):
        """
        Attempts to read config.json. If this does not exist, create a blank template.
        """
        self.fileName = 'config.json'
        if path.exists(self.fileName):
            self.read()
        else:
            self.folder_Main = designate_folder("Please designate a folder where you would like to store your .csv files. A new folder will be created there.")
            self.folder_BS = create_folder(self.folder_Main, "Bank Statements")
            self.folder_BS_New = create_folder(self.folder_BS, "New")
            self.folder_BS_Old = create_folder(self.folder_BS, "Old")
            self.folder_BS_Processed = create_folder(self.folder_BS, "Processed")

        self.config_correct = self.check_config()
        self.write()

    def write(self):
        """
        Write the local config file
        """
        with open(self.fileName, 'w') as jsonfile:
            json.dump(self.__dict__, jsonfile)
            print('Configuration file written successfully.')

    def read(self):
        """
        Read the local JSON file
        """
        with open(self.fileName) as infile:
            config_dict = json.load(infile)
            for k, v in config_dict.items():
                setattr(self, k, v)
        print("Configuration file read successfully.")

    def check_config(self):
        """
        Checks if the configuration is correct. This means that all folders are existing and designated.

        :return: True if the configuration is correct, otherwise False.
        """
        config_fault = False
        for value in {value for key, value in self.__dict__.items() if 'folder' in key}:  # wat is dit nu weer?
            if not os.path.exists(value):
                config_fault = True
        if config_fault is False:
            print("The configuration is correct. All folders are identified and exist.")
            return True
        else:
            return False
