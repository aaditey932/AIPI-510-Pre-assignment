# Import Necessary Libraries #
import pandas as pd
import argparse



# Function That Sorts The 'cc_info' CSV File By The Values In The 'city' Column #
def sortcsv(input_csv):

    csv_file = pd.read_csv(input_csv) # Reads Input CSV File And Stores It In 'csv_file'
    dataframe = pd.DataFrame(csv_file) # Converts CSV File Into Dataframe
    dataframe = dataframe.sort_values(by='city',ascending=True) # Sorts Dataframe By 'city' Column In Ascending Order
    dataframe.to_csv('sorted_cc_info.csv',index=False) # Stores Dataframe Into 'sorted_cc_info.csv' File




# Main Entry Point Of The Script #
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Sort credit card info by city names') # Creates Argument Parser To Handle Command Line Arguments
    parser.add_argument('input_file', help = 'The input csv file') # Adds Argument To Input CSV File
    args = parser.parse_args() # Parses The Command Line Arguments

    sortcsv(args.input_file) # Calls The 'sortcsv' Function With The Input File Given By User In Command Line