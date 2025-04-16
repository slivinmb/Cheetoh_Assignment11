# File Name : main.py
# Student Name: Michael Slivinski and Will Claus
# email: slivinmb@mail.uc.edu, clausws@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  

# Brief Description of what this module does: 
# Citations: 

# Anything else that's relevant:

from cleaningPackage.cleanCSV import *
from csvPackage.saveCSV import *
from zipPackage.zipCode import *

if __name__ == "__main__":
    cleaner = FuelDataCleaner("fuelPurchaseData.csv")
    cleaner.remove_duplicates()
    cleaner.remove_anomalies()
    cleaner.clean_gross_price()

    saver = FuelDataSaver(cleaner.get_cleaned_data())
    saver.save_cleaned_file()

    
    
    