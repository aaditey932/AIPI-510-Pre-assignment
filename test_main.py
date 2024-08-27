## Import Necessary Libraries ##
import unittest
import main
import pandas as pd
import pandas.testing as pdt


## Unit Test Class ##
class TestSortCSV(unittest.TestCase):
    
    # Setup Envionment Before Each Test #
    def setUp(self):

        main.sortcsv('cc_info.csv') # Sorting Input File
        self.sorted_csv = pd.read_csv('sorted_cc_info.csv') # Reads Input CSV File
        self.sorted_df = pd.DataFrame(self.sorted_csv) # Converts CSV File Into Dataframe



    # Test That Verifies Shape Of Output File -> 'sorted_cc_info.csv' #
    def test_shapeof_sortedcsv(self):

        number_of_rows = (984,5) # Expected Shape 
        number_of_rows_csv = self.sorted_df.shape # Shape of Output File
        self.assertEqual(number_of_rows,number_of_rows_csv) # Compares Both Shapes



    # Test That Verifies If Output File Is Sorted Correctly #
    def test_sortedcsv(self):

        expected_csv = pd.read_csv('expected_sorted_cc_info.csv') # Reads Expected CSV File
        expected_df = pd.DataFrame(expected_csv) # Converts Expected CSV File Into Dataframe
        pdt.assert_frame_equal(expected_df,self.sorted_df) # Compares Both Files To Verify Sorting




## Main Entry Point Of The Script ##
if __name__ == '__main__':
    unittest.main()