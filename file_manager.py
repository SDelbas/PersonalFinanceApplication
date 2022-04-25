import os
import shutil
import warnings
from datetime import date, datetime
import pandas as pd

from configuration import Configuration

# # Initialize primary file locations (Should be linked to dash app later on)
# configuration = Configuration()
# csv_folder_archive = os.path.join(configuration.location_folder, 'csv\\csv-archive')  # Storage location for old CSV files
# csv_folder_new = os.path.join(configuration.location_folder, 'csv\\csv-new')  # Storage location for new CSV files
# csv_folder_master = os.path.join(configuration.location_folder, 'csv\\csv-master')

# Initialize primary file locations (Should be linked to dash app later on)
csv_folder_archive = os.path.join(os.getcwd(), 'csv\\csv-archive')  # Storage location for old CSV files
csv_folder_new = os.path.join(os.getcwd(), 'csv\\csv-new')  # Storage location for new CSV files
csv_folder_master = os.path.join(os.getcwd(), 'csv\\csv-master')


def importer():
    files_to_be_processed = finder()
    df_raw = reader(files_to_be_processed)
    df_raw = formatter(df_raw)
    writer(df_raw)
    # Test code
    df_raw.to_pickle('./dataframe.pkl')
    df_raw = set_starting_values(df_raw)
    return df_raw


def finder():
    # main_folder = os.getcwd()  # Main folder where CSV files will be kept. Currently, set to main program folder.

    # Find new CSV files
    print("")
    print("Looking for new CSV files")
    files_new = [f for f in os.listdir(csv_folder_new) if os.path.isfile(os.path.join(csv_folder_new, f))]  # Create a list containing each file f in the main program folder
    print("Found " + str(len(files_new)) + ' new CSV files:')
    for f in files_new:
        print(os.path.join(csv_folder_new, f))
    files_new_return = [csv_folder_new + "\\" + files for files in files_new]
    print("")
    print("")

    # Find old CSV folders
    print("Looking for archived CSV folders")
    folders_archive = [f for f in os.listdir(csv_folder_archive) if os.path.isdir(os.path.join(csv_folder_archive, f))]  # Create a list containing each file f in the main program folder
    print("Found " + str(len(folders_archive)) + ' archived CSV folders:')
    for f in folders_archive:
        print(os.path.join(csv_folder_archive, f))
    print("")
    print("")

    # Find CSV master files
    print("Looking for CSV master files")
    files_master = [f for f in os.listdir(csv_folder_master) if os.path.isfile(os.path.join(csv_folder_master, f))]  # Create a list containing each file f in the main program folder
    print("Found " + str(len(files_master)) + ' CSV master files:')
    for f in files_master:
        print(os.path.join(csv_folder_master, f))

    if len(files_master) != 0:
        files_master_return = [[csv_folder_master + "\\" + files for files in files_master][-1]]
    else:
        files_master_return = []
    print("")
    print("")

    # Return all files that must be processed
    files_master_return.extend(files_new_return)
    files_to_be_processed = files_master_return
    return files_to_be_processed


def writer(df):
    # Create an archive folder if it does not exist yet.
    if not os.path.isdir(csv_folder_master):
        print()
        print('Creating new folder at ' + csv_folder_master)
        os.mkdir(csv_folder_master)

    location = csv_folder_master + '\\MASTER' + date.today().strftime('-%Y-%m-%d') + '.csv'
    df.to_csv(location, index=True, index_label=['Uitvoeringsdatum', 'Rekeningnummer', 'Volgnummer'])
    # mover()
    return


def mover():
    source = csv_folder_new
    destination = csv_folder_archive + "\\" + date.today().strftime('%Y-%m-%d')

    if len(os.listdir(source)) != 0:
        # Create an archive folder if it does not exist yet.
        if not os.path.isdir(destination):
            print()
            print('Creating new folder at ' + destination)
            os.mkdir(destination)

        # Move all files from source to destination
        files_to_be_processed = os.listdir(source)
        for files in files_to_be_processed:
            print('Moving the following file: ' + files + ' to ' + destination, end='')
            shutil.move(source + "\\" + files, destination + "\\" + files)
            print('-' * (len(max(files_to_be_processed, key=len)) - len(files) + 5) + 'Succes')
    return


def reader(files_to_be_processed):
    # Dictionary containing all information regarding different bank CSV files.
    csv_dict = {
        'MASTER': {
            'Required': {
                'filepath_or_buffer': None,
                'sep': ',',
                # 'thousands': None,
                # 'decimal': None,
                'keep_default_na': True,
                'index_col': False,
                # 'header': None,
                # 'names': None,
                'dtype': {
                    'Uitvoeringsdatum': str,
                    'Valutadatum': str,
                    'Bedrag': float,
                },
                'parse_dates': [4, 5],
                'dayfirst': True,
                'infer_datetime_format': True,
                # 'encoding': None,
            },
            'Optional': {
                'Bank': 'MASTER',
            }
        },
        'ING': {
            'Required': {
                'filepath_or_buffer': None,
                'sep': ';',
                'thousands': '.',
                'decimal': ',',
                'keep_default_na': True,
                'index_col': False,
                'header': 0,
                'names': ['Rekeningnummer', 'Naam van de rekening', 'Rekening tegenpartij', 'Volgnummer', 'Uitvoeringsdatum', 'Valutadatum', 'Bedrag', 'Munteenheid', 'Omschrijving', 'Detail van de omzet', 'Bericht'],
                'dtype': {
                    'Uitvoeringsdatum': str,
                    'Valutadatum': str,
                    'Bedrag': float,
                    'Volgnummer': str,
                },
                'parse_dates': [4, 5],
                'dayfirst': True,
                'infer_datetime_format': True,
                'encoding': 'windows_1250',
            },
            'Optional': {
                'Bank': 'ING',
                'names_reformatted': ['Uitvoeringsdatum', 'Valutadatum', 'Rekeningnummer', 'Bedrag', 'Munteenheid', 'Volgnummer', 'Rekening tegenpartij', 'Omschrijving', 'Naam van de rekening', 'Detail van de omzet', 'Bericht'],
                'Prefix': 6
            }
        },
        'BNP': {
            'Required': {
                'filepath_or_buffer': None,
                'sep': ';',
                'thousands': '.',
                'decimal': ',',
                'keep_default_na': True,
                'index_col': False,
                'header': 0,
                'names': ['Volgnummer', 'Uitvoeringsdatum', 'Valutadatum', 'Bedrag', 'Munteenheid', 'Rekeningnummer', 'Type verrichting', 'Tegenpartij', 'Naam van de tegenpartij', 'Mededeling', 'Details', 'Status', 'Reden van weigering'],
                'dtype': {
                    'Uitvoeringsdatum': str,
                    'Valutadatum': str,
                    'Bedrag': float,
                    'Volgnummer': str,
                },
                'parse_dates': [1, 2],
                'dayfirst': True,
                'infer_datetime_format': True,
                'encoding': 'windows_1250',
            },
            'Optional': {
                'Bank': 'BNP',
                'names_reformatted': ['Uitvoeringsdatum', 'Valutadatum', 'Rekeningnummer', 'Bedrag', 'Munteenheid', 'Volgnummer', 'Tegenpartij', 'Mededeling', 'Naam van de tegenpartij', 'Details', 'Status', 'Reden van weigering'],
                'Prefix': 6
            }
        },
    }

    # Import new CSV files and latest MASTER file
    csv_df_import = None
    for files in files_to_be_processed:
        print('Importing the following file: ' + files, end='')
        match len(os.path.basename(files)):  # Zie re.match voor uitgebreide optie?
            case 21:
                csv_dict['MASTER']['Required']['filepath_or_buffer'] = files
                csv_df_import = pd.concat([csv_df_import, read_csv(**csv_dict['MASTER'])], ignore_index=True, sort=False)
            case 24:
                csv_dict['BNP']['Required']['filepath_or_buffer'] = files
                csv_df_import = pd.concat([csv_df_import, read_csv(**csv_dict['BNP'])], ignore_index=True, sort=False)
            case 47:
                csv_dict['ING']['Required']['filepath_or_buffer'] = files
                csv_df_import = pd.concat([csv_df_import, read_csv(**csv_dict['ING'])], ignore_index=True, sort=False)
            case __:
                print('-' * (len(max(files_to_be_processed, key=len)) - len(files) + 5) + 'Failed')
                raise Exception("Unidentified bank account found. Please check the structure of new files and MASTER files.")
        print('-' * (len(max(files_to_be_processed, key=len)) - len(files) + 5) + 'Succes')

    # Convert columns to datetime
    for i in ['Uitvoeringsdatum', 'Valutadatum']:
        csv_df_import[i] = pd.to_datetime(csv_df_import[i], yearfirst=True)

    # Sort columns by descending date
    csv_df_import.sort_values(by='Uitvoeringsdatum', ascending=False, inplace=True)

    # Reset indexes and drop them
    csv_df_import.reset_index(drop=True, inplace=True)

    # Remove duplicate rows, based on 'Rekeningnummer' and'Volgnummer'
    csv_df_import_rows = csv_df_import.shape[0]
    csv_df_import.drop_duplicates(subset=['Volgnummer', 'Rekeningnummer'], inplace=True)
    print()
    if csv_df_import_rows - csv_df_import.shape[0] > 0:
        print(str(csv_df_import_rows - csv_df_import.shape[0]) + ' rows were dropped')

    # Check if the 'Categorie' column exists and add it to the Unassigned category
    if 'Categorie' not in csv_df_import.columns:
        csv_df_import['Categorie'] = -100
    else:
        csv_df_import['Categorie'].fillna(-100)

    # Check if the 'Comment' column exists and add it to the Unassigned category
    if 'Comment' not in csv_df_import.columns:
        csv_df_import['Comment'] = -100
    else:
        csv_df_import['Comment'].fillna(-100)

    return csv_df_import


def read_csv(**csv_dict):
    # Read the CSV file
    df = pd.read_csv(
        **csv_dict['Required']
    )

    if csv_dict['Optional']['Bank'] != 'MASTER':
        # Order the columns as desired.
        df = df[csv_dict['Optional']['names_reformatted']]

        if csv_dict['Optional']['Bank'] == 'ING':
            # Generate 'Volgnummer' of the following format: YYYY-XXXXX (Year - Number)
            df['Volgnummer'] = df['Uitvoeringsdatum'].dt.year.astype(str) + '-' + df['Volgnummer'].str.zfill(5)

            # Remove excess spaces in 'Details' column
            while df['Detail van de omzet'].str.count('  ').sum() > 0:
                df['Detail van de omzet'] = df['Detail van de omzet'].str.replace('  ', ' ')

        if csv_dict['Optional']['Bank'] == 'BNP':
            # Remove rows where the 'Volgnummer' is shorter than 10 characters (Volgnummer not yet defined by BNP)
            df = df.drop(df[df['Volgnummer'].str.len() < 10].index)

        # Add prefix
        df.columns = [csv_dict['Optional']['Bank'] + '-' + i if ix >= csv_dict['Optional']['Prefix'] else i for ix, i in enumerate(df.columns)]
    return df


def formatter(df_raw):
    # Set correct dtypes
    for column in df_raw.columns:
        if column in ['Uitvoeringsdatum', 'Valutadatum']:
            df_raw[column] = df_raw[column].astype('datetime64[ns]')
        elif column in ['Bedrag']:
            df_raw[column] = df_raw[column].astype('float64')
        else:
            df_raw[column] = df_raw[column].astype('object')

    # Reformat df_raw to use a unique Multi Index
    df_raw.set_index(['Uitvoeringsdatum', 'Rekeningnummer', 'Volgnummer'], inplace=True)
    df_raw.sort_values(by=['Uitvoeringsdatum', 'Rekeningnummer', 'Volgnummer'], ascending=False, inplace=True)
    return df_raw


def set_starting_values(df_raw):
    warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)
    df_raw.loc[(datetime.strptime('2014/08/01', '%Y/%m/%d'), 'BE75035892604751', '2014-00000'), 'Bedrag'] = 4070.12
    df_raw.loc[(datetime.strptime('2014/08/01', '%Y/%m/%d'), 'BE29001430601264', '2014-00000'), 'Bedrag'] = 389.78
    warnings.simplefilter(action='default', category=pd.errors.PerformanceWarning)
    return df_raw
