#!/usr/bin/env python3
import logging
import pandas as pd

logging.basicConfig(format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')


class Utils:
    """A class for helper functions"""
    def __init__(self):
        logging.info("Utils object created")

    def missing_values_table(self, df):
        """Function to calculate missing values by column
        """
        mis_val = df.isnull().sum()

        mis_val_percent = 100 * df.isnull().sum() / len(df)

        mis_val_dtype = df.dtypes

        mis_val_table = pd.concat([mis_val, mis_val_percent, mis_val_dtype], axis=1)

        mis_val_table_ren_columns = mis_val_table.rename(columns = {
            0 : 'Missing Values', 1 : '% of Total Values', 2: 'Dtype'})
        
        mis_val_table_ren_columns = mis_val_table_ren_columns[
                mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
                        '% of Total Values', ascending=False).round(1)

        logging.info("Your selected dataframe has " + str(df.shape[1]) + 
                " columns.\n" + "There are " + 
                str(mis_val_table_ren_columns.shape[0]) + 
                " columns that have missing values.")
        return mis_val_table_ren_columns

    def format_float(self, value):
        return f'{value:,.2f}'

    def find_agg(self, df:pd.DataFrame, agg_column:str, agg_metric:str, col_name:str, top:int, order=False )->pd.DataFrame:
        """A method for aggregation
        """
        new_df = df.groupby(agg_column)[agg_column].agg(agg_metric).reset_index(name=col_name).sort_values(by=col_name, ascending=order)[:top]

        return new_df

    def convert_bytes_to_megabytes(self, df, bytes_data):
        """
            This function takes the dataframe and the column which has the bytes values
            returns the megabytesof that value

            Args:
            -----
            df: dataframe
            bytes_data: column with bytes values

            Returns:
            --------
            A series
        """

        megabyte = 1*10e+5
        df[bytes_data] = df[bytes_data] / megabyte

        return df[bytes_data]
