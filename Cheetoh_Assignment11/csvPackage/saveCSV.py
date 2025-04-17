# File Name : saveCSV.py
# Student Name: Michael Slivinski and Will Claus
# email: slivinmb@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment shows us how to connect to an api and add zip codes to a csv file.

# Brief Description of what this module does: This module saves the cleaned data to a new csv.
# Citations: 
# www.chatgpt.com
# Anything else that's relevant:


import os

class FuelDataSaver:
    '''
    This module defines the FuelDataSaver class, which is responsible for saving a cleaned
    pandas DataFrame to a CSV file. It ensures the output directory exists and handles
    file creation in a specified folder and filename.
    '''
    def __init__(self, dataframe):
        self.df = dataframe

    def save_cleaned_file(self, folder='dataPackage/data', filename='cleanedData.csv'):
        if not os.path.exists(folder):
            os.makedirs(folder)
        output_path = os.path.join(folder, filename)
        self.df.to_csv(output_path, index=False)
        print(f"Cleaned file saved to: {output_path}")