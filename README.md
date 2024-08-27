# AIPI-510-Pre-assignment

# CSV Sorting Project

## Overview

This project includes a Python script and unit tests for sorting CSV files. The main functionality is provided by the `sortcsv` function, which sorts a specified column in a CSV file and saves the result to a new file. The project also includes unit tests to verify the correctness of the sorting functionality.

## Files

- `main.py`: Contains the `sortcsv` function for sorting CSV files.
- `test_main.py`: Contains unit tests for the `sortcsv` function.
- `cc_info.csv`: Sample input CSV file for testing.
- `expected_sorted_cc_info.csv`: Expected output CSV file used for testing.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aaditey932/AIPI-510-Pre-assignment.git

2. Navigate to the project directory:

   cd <project-directory>

3. Create and activate a virtual environment:

   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

5. Install the required packages:

   pip install -r requirements.txt

## Usage

1. Run the Sorting Script:

   python main.py cc_info.csv

2. View the Output:

   The sorted data will be saved in the file 'sorted_cc_info.csv'.

## Installation

1. Run Unit Tests:

   python -m unittest test_main.py

   This will execute the tests and provide output indicating whether the tests passed or failed.
