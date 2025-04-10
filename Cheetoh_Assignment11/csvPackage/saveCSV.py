# File Name : saveCSV.py
# Student Name: Michael Slivinski and Will Claus
# email: slivinmb@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  

# Brief Description of what this module does: 
# Citations: 

# Anything else that's relevant:


import os

class FuelDataSaver:
    def __init__(self, dataframe):
        self.df = dataframe

    def save_cleaned_file(self, folder='dataPackage/data', filename='cleanedData.csv'):
        if not os.path.exists(folder):
            os.makedirs(folder)
        output_path = os.path.join(folder, filename)
        self.df.to_csv(output_path, index=False)
        print(f"Cleaned file saved to: {output_path}")