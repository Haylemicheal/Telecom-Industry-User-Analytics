import unittest
import os, sys
import numpy
import pandas

sys.path.append(os.path.abspath(os.path.join('..')))

from scripts.dataloader import DataLoader
from scripts.utils import Utils

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.dataloader = DataLoader('../data', 'sample.csv')
        self.df = self.dataloader.read_csv()
        self.ut = Utils()
    
    def test_format_float(self):
        value = 2.3444445
        self.assertEqual(self.ut.format_float(value), '2.34')
        self.assertEqual(self.ut.format_float(-5.77778789), '-5.78')

    def test_missing_values_table(self):
        self.assertEqual(self.ut.missing_values_table(self.df).shape, (12,3))

    def test_bytes_to_megabytes(self):
        myarray = numpy.array([[1048576], [1024*4*1000]])
        colnames = ['bytes']
        df = pandas.DataFrame(myarray, columns=colnames)
        self.assertEqual(self.ut.convert_bytes_to_megabytes(df, 'bytes').shape,(2,))
        

if __name__ == '__main__':
    unittest.main()

