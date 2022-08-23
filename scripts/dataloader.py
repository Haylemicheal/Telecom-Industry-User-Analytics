import os
import pandas as pd


class DataLoader:
    """DataLoader class"""
    def __init__(self, dir_name, file_name):
        """Constructor of the Dataloader class
        Attributes:
            dir_name: Directory name
            file_name: The name of the file
        """
        self.dir_name = dir_name
        self.file_name = file_name

    def read_csv(self):
        """A method for reading csv files
        return:
            pandas dataframe
        """
        os.chdir(self.dir_name)
        df = pd.read_csv(self.file_name)
        return df

    def read_excel(self):
        """A method for reading excel files
        return:
            pandas dataframe
        """
        os.chdir(self.dir_name)
        df = pd.read_excel(self.file_name)
        return df
