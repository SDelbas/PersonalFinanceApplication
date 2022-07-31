import locale

import pandas as pd
import os
from find_csv import find_csv


def read_csv():
    # Specify folderMain containing new .csv files to be imported
    dir_path_new = os.path.dirname(os.path.realpath(__file__))
    dir_path_new = os.path.join(dir_path_new, "csv\\csv-new")

    # Generate list of .csv files to be imported
    files = find_csv()

    df_new_import = []

    for files_num in files:

        if len(files_num) == 47:  # Read an ING bank account CSV
            # print(files_num)
            df_new_import.append(read_csv_ing(dir_path_new, files_num))

        elif len(files_num) == 24:  # Read a BNP bank account CSV
            df_new_import.append(read_csv_bnp(dir_path_new, files_num))

        elif len(files_num) == 19:
            df_new_import.append(read_csv_main(dir_path_new, files_num))

        else:
            raise Exception("Unidentified bank account")

    dt = ()
    for df_num in df_new_import:
        if len(dt) == 0:
            dt = df_num
        else:
            dt = pd.concat([dt, df_num], ignore_index=True, sort=False)

    dt['Uitvoeringsdatum'] = pd.to_datetime(dt['Uitvoeringsdatum'], format='%d/%m/%Y')

    # dt = dt.sort_values('Uitvoeringsdatum', ascending=False)
    # locale.setlocale(locale.LC_NUMERIC, 'nl_BE')
    # dt["Bedrag"] = round(dt["Bedrag"].apply(locale.atof), 2)
    dt = dt.sort_values(by='Uitvoeringsdatum', ascending=False)
    dt = dt.reset_index(drop=True)
    return dt


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Read CSV's from an ING bank account
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def read_csv_ing(dir_path, files_num):
    # Read the CSV file
    df = pd.read_csv(
        filepath_or_buffer=os.path.join(dir_path, files_num),
        sep=";",
        thousands='.',
        decimal=',',
        keep_default_na=True,
        index_col=False,
        header=0,
        names=['Rekeningnummer', 'Naam van de rekening', 'Rekening tegenpartij', 'Volgnummer', 'Uitvoeringsdatum', 'Valutadatum', 'Bedrag', 'Munteenheid', 'Omschrijving', 'Detail van de omzet', 'Bericht'],
        dtype=
        {
            'Rekeningnummer': str,
            'Naam van de rekening': str,
            'Rekening tegenpartij': str,
            'Volgnummer': str,
            'Uitvoeringsdatum': str,
            'Valutadatum': str,
            'Bedrag': float,
            'Munteenheid': str,
            'Omschrijving': str,
            'Detail van de omzet': str,
            'Bericht': str
        },
        parse_dates=[4, 5],
        dayfirst=True,
        infer_datetime_format=True,
        encoding="windows_1250",
    )

    # Order the columns as desired.
    df = df[['Uitvoeringsdatum', 'Valutadatum', 'Rekeningnummer', 'Bedrag', 'Munteenheid', 'Volgnummer', 'Rekening tegenpartij', 'Omschrijving', 'Naam van de rekening', 'Detail van de omzet', 'Bericht']]

    # Generate 'Volgnummer' of the following format: YYYY-XXXXX (Year - Number)
    df['Volgnummer'] = df['Uitvoeringsdatum'].dt.year.astype(str) + '-' + df['Volgnummer'].str.zfill(5)

    # Remove excess spaces in 'Details' column
    while df['Detail van de omzet'].str.count('  ').sum() > 0:
        # print(df['Details'].str.count('  ').sum())
        df['Detail van de omzet'] = df['Detail van de omzet'].str.replace('  ', ' ')

    # Add ING prefix
    df.columns = ['ING-' + i if ix > 5 else i for ix, i in enumerate(df.columns)]
    return df


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Read CSV's from a BNP bank account
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def read_csv_bnp(dir_path, files_num):
    # Read the CSV file
    df = pd.read_csv(
        filepath_or_buffer=os.path.join(dir_path, files_num),
        sep=";",
        thousands='.',
        decimal=',',
        keep_default_na=True,
        index_col=False,
        header=0,
        names=['Volgnummer', 'Uitvoeringsdatum', 'Valutadatum', 'Bedrag', 'Munteenheid', 'Rekeningnummer', 'Type verrichting', 'Tegenpartij', 'Naam van de tegenpartij', 'Mededeling', 'Details', 'Status', 'Reden van weigering'],
        dtype=
        {
            'Volgnummer': str,
            'Uitvoeringsdatum': str,
            'Valutadatum': str,
            'Bedrag': float,
            'Munteenheid': str,
            'Rekeningnummer': str,
            'Type verrichting': str,
            'Tegenpartij': str,
            'Naam van de tegenpartij': str,
            'Mededeling': str,
            'Details': str,
            'Status': str,
            'Reden van weigering': str
        },
        parse_dates=[1, 2],
        dayfirst=True,
        infer_datetime_format=True,
        encoding="windows_1250",
    )

    # Remove rows where the 'Volgnummer' is shorter than 10 characters (Volgnummer not yet defined by BNP)
    df = df.drop(df[df['Volgnummer'].str.len() < 10].index)

    # Order the columns as desired.
    df = df[['Uitvoeringsdatum', 'Valutadatum', 'Rekeningnummer', 'Bedrag', 'Munteenheid', 'Volgnummer', 'Tegenpartij', 'Mededeling', 'Naam van de tegenpartij', 'Details', 'Status', 'Reden van weigering']]

    # Add BNP prefix
    df.columns = ['BNP-' + i if ix > 5 else i for ix, i in enumerate(df.columns)]

    return df


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Read CSV's from a BNP bank account
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def read_csv_main(dir_path, files_num):
    # Read the CSV file
    df = pd.read_csv(
        filepath_or_buffer=os.path.join(dir_path, files_num),
        sep=",",
        #thousands='.',
        #decimal=',',
        keep_default_na=True,
        index_col=False,
        # header=0,
        # names=['Volgnummer', 'Uitvoeringsdatum', 'Valutadatum', 'Bedrag', 'Munteenheid', 'Rekeningnummer', 'Type verrichting', 'Tegenpartij', 'Naam van de tegenpartij', 'Mededeling', 'Details', 'Status', 'Reden van weigering'],
        dtype=
        {
            'Uitvoeringsdatum': str,
            'Valutadatum': str,
            'Bedrag': float,
        },
        parse_dates=[0, 1],
        dayfirst=True,
        infer_datetime_format=True,
        # encoding="windows_1250",
    )
    return df
