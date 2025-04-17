# File Name : cleanCSV.py
# Student Name: Michael Slivinski and Will Claus
# email: slivinmb@mail.uc.edu, clausws@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment shows us how to connect to an api and add zip codes to a csv file.


# Brief Description of what this module does: This module shows the clean data 

# Citations: 

# Anything else that's relevant:


import pandas as pd
import os

class FuelDataCleaner:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath)

    def clean_gross_price(self):
        self.df['Gross Price'] = self.df['Gross Price'].apply(lambda x: f"{float(x):.2f}")

    def remove_duplicates(self):
        original_count = len(self.df)
        self.df.drop_duplicates(subset=['Transaction Number'], inplace=True)
        removed = original_count - len(self.df)
        print(f"Removed {removed} duplicate row(s) based on 'Transaction Number'.")

    def remove_anomalies(self, column='Fuel Type', anomaly_value='Pepsi', anomaly_file='dataPackage/data/dataAnomalies.csv'):
        anomalies = self.df[self.df[column] == anomaly_value]
        self.df = self.df[self.df[column] != anomaly_value]

        if not anomalies.empty:
            folder = os.path.dirname(anomaly_file)
            if not os.path.exists(folder):
                os.makedirs(folder)
            anomalies.to_csv(anomaly_file, index=False)
            print(f"Anomalies saved to: {anomaly_file}")
        else:
            print("No anomalies found to remove.")

    def get_cleaned_data(self):
        return self.df