import pandas as pd
import datetime


def main(df_raw):
    # Code overview The main purpose of this block is to fill out and clear the raw data contained in the dataframe. A dataframe is created containing empty (0 value) transactions for each unique bank account, for every day since the
    # start of the monitoring. This dataframe is combined with the raw data dataframe and filtered to remove unnecessary empty transactions.

    # Relevant information
    # https://stackoverflow.com/questions/44978196/pandas-filling-missing-dates-and-values-within-group
    # https://stackoverflow.com/questions/53645882/pandas-merging-101

    # Test code to import dataFrame
    # df_raw = pd.read_pickle('dataframe.pkl')

    # Create the dataframe containing the filler data
    # Establish date range from the oldest date to current date
    date_min = min(df_raw.index.get_level_values(0))
    date_max = datetime.date.today()
    dates = pd.date_range(start=date_min, end=date_max, freq='D')

    # Establish uique bank accounts
    accounts = df_raw.index.get_level_values(1).unique().tolist()

    # Establish unique transaction numbers
    volgnummers = df_raw.index.get_level_values(2).unique().tolist()

    # Create the new Multi Index
    df_padding_index = pd.MultiIndex.from_product((dates, accounts, ['NaN']), names=['Uitvoeringsdatum', 'Rekeningnummer', 'Volgnummer'])

    # Create the new dataframe
    df_padding = pd.DataFrame(index=df_padding_index, columns=df_raw.columns).fillna('NaN')
    df_padding['Bedrag'] = 0
    df_padding['Valutadatum'] = df_padding['Valutadatum'].astype('datetime64[ns]')
    df_padding['Bedrag'] = df_padding['Bedrag'].astype('float64')

    # Merge the two dataframes
    df_extended = pd.concat([df_raw, df_padding])
    df_extended = df_extended.sort_values(by=['Uitvoeringsdatum', 'Rekeningnummer', 'Volgnummer'], ascending=False)

    # Split the dataframe into two dataframes. One containing the unique indexes for 'Uitvoeringsdatum' and 'Rekeningnummer' and one containing the duplicates.
    df_merged_uniques = df_extended[~df_extended.droplevel(2).index.duplicated(keep=False)]
    dj_merged_duplicates = df_extended[df_extended.droplevel(2).index.duplicated(keep=False)]

    # Remove the NaN rows for 'Volgnummer' from the duplicates
    dj_merged_duplicates = dj_merged_duplicates[dj_merged_duplicates.droplevel(2).index.duplicated(keep='first')]

    # Re-merge the dataframes
    df_extended = pd.concat([df_merged_uniques, dj_merged_duplicates]).sort_values(by=['Uitvoeringsdatum', 'Rekeningnummer', 'Volgnummer'], ascending=False)

    return df_extended
