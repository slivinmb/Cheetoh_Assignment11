# File Name : main.py
# Student Name: Michael Slivinski and Will Claus
# email: slivinmb@mail.uc.edu, clausws@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment shows us how to connect to an api and add zip codes to a csv file.

# Brief Description of what this module does: This module instantiates classes and invokes methods that clean the data and print to a new csv. 
# Citations: 
# www.chatgpt.com
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

    if __name__ == "__main__":
    # Step 1: Clean the data
        cleaner = FuelDataCleaner("fuelPurchaseData.csv")
    cleaner.remove_duplicates()
    cleaner.remove_anomalies()
    cleaner.clean_gross_price()
    df = cleaner.get_cleaned_data()

    # Step 2: Fill ZIPs in Full Address (first 5 missing only)
    api_key = "834cf3b0-1b40-11f0-b378-b5b61bee0da7"
    filler = ZipCodeFiller(api_key)
    updated_df = filler.fill_missing_zip_codes(df, address_col="Full Address", max_updates=5)

    # Step 3: Save updated DataFrame to cleanedData.csv
    saver = FuelDataSaver(updated_df)
    saver.save_cleaned_file()

    print("ZIP code filling complete. Cleaned data saved to dataPackage/data/cleanedData.csv.")



  

    
    
    