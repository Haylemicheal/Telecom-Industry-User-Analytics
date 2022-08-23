import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

from scripts.dataloader import DataLoader

class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.dir_name = "../data"

    def test_read_csv(self):
        """Test the readcsv method"""
        filename = "sample.csv"
        dataloader = DataLoader(self.dir_name, filename)
        pd = dataloader.read_csv()
        col1 = pd.columns[0]
        self.assertEqual(col1, "Bearer Id")

if __name__ == '__main__':
    unittest.main()
