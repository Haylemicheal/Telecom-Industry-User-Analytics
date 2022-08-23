#!/usr/bin/env python3

class DataUnderstanding:
    """Class for understanding the data"""
    def __init__(self, dataframe):
        """Constructor
        Attributes:
            dataframe: Pandas dataframe
        """
        self.df = dataframe

    def peak_data(self, rows):
        """Peak some rows from the data
        Attributes:
            rows: The number of rows to be picked
        return:
            dataframe
        """
        return self.df.head(rows)

    def data_dimension(self):
        """Return the shape of the dataframe"""
        return self.df.shape

    def get_datatypes(self):
        """Get the datatype of each column"""
        return self.df.dtypes

    def get_descriptive_stat(self):
        """Statstical description gives us the Count, Mean, Standard Deviation,
        Minimum Value, 25th Percentile, Median, 75th Percentile, and Maximum Value
        """
        return self.df.describe()

    def attributes_correlation(self):
        """A method for correlation of attributes. We use pearson algorithm in this case
        """
        return self.df.corr(method= 'pearson')

    def get_skew(self):
        """Get skew of univarian data distribution"""
        return self.df.skew()
