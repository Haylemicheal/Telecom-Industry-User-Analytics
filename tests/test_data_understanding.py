import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from scripts.dataloader import DataLoader
from scripts.data_understanding import DataUnderstanding

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.dataloader = DataLoader('../data', 'sample.csv')
        self.df = self.dataloader.read_csv()
        self.du = DataUnderstanding(self.df)

    def test_peak_data(self):
        top5 = self.du.peak_data(5)
        self.assertEqual(top5.shape, (5,55))

    def test_data_dimension(self):
        shape = self.du.data_dimension()
        self.assertEqual(shape, (10,55))

    def test_get_datatypes(self):
        datatypes = self.du.get_datatypes()
        self.assertEqual(datatypes[0],"float64")
        self.assertEqual(datatypes[1],"object")
        self.assertEqual(datatypes[2],"int64")

    def test_get_descriptive_stat(self):
        desc = self.du.get_descriptive_stat()
        self.assertEqual(desc.shape, (8,50))

    def test_attributes_correlation(self):
        corr = self.du.attributes_correlation()
        self.assertEqual(corr.shape, (50,50))

    def test_get_skew(self):
        skew = self.du.get_skew()
        self.assertEqual(skew[0], -1.7787811838437169)

if __name__ == '__main__':
    unittest.main()
