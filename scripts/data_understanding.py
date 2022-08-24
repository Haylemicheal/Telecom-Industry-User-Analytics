#!/usr/bin/env python3
import logging

logging.basicConfig(format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

class DataUnderstanding:
    """Class for understanding the data"""
    def __init__(self, dataframe):
        """Constructor
        Attributes:
            dataframe: Pandas dataframe
        """
        self.df = dataframe
        logging.info("The data understanding object is created")


    def peak_data(self, rows):
        """Peak some rows from the data
        Attributes:
            rows: The number of rows to be picked
        return:
            dataframe
        """
        logging.info("Peak {} rows".format(str(rows)))
        return self.df.head(rows)

    def data_dimension(self):
        """Return the shape of the dataframe"""
        logging.info("The shape of the data is {}".format(self.df.shape))
        return self.df.shape

    def get_datatypes(self):
        """Get the datatype of each column"""
        logging.info("List datatypes of each column")
        return self.df.dtypes

    def get_descriptive_stat(self):
        """Statstical description gives us the Count, Mean, Standard Deviation,
        Minimum Value, 25th Percentile, Median, 75th Percentile, and Maximum Value
        """
        logging.info("Describe the data")
        return self.df.describe()

    def attributes_correlation(self):
        """A method for correlation of attributes. We use pearson algorithm in this case
        """
        logging.info("Print out the correlation of the data")
        return self.df.corr(method= 'pearson')

    def get_skew(self):
        """Get skew of univarian data distribution"""
        return self.df.skew(numeric_only=True)
