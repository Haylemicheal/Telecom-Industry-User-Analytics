#!/usr/bin/env python3
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

class DataCleaning:
    """Class for data cleaning"""
    def normalizer(self, X):
        """A method to normalize data
        """
        scaler = Normalizer().fit(X)
        normalizedX = scaler.transform(X)
        return normalizedX

    def rescale_data(self, X):
        """Rescaling our data"""
        scaler = MinMaxScaler(feature_range=(0, 1))
        rescaledX = scaler.fit_transform(X)
        return rescaledX

    def standardize(self, X):
        """Standardize our data
        """
        scaler = StandardScaler().fit(X)
        rescaledX = scaler.transform(X)
