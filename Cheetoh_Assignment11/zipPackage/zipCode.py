# File Name : zipCode.py
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

import requests

class ZipCodeFiller:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://app.zipcodebase.com/api/v1/search"

    def fetch_zip_code(self, city, country='US'):
        try:
            params = {
                "apikey": self.api_key,
                "city": city,
                "country": country
            }
            response = requests.get(self.url, params=params)
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", {}).get(city, [])
                if results:
                    return results[0]
        except Exception:
            pass
        return None

    def fill_missing_zip_codes(self, df, city_col='City', zip_col='ZipCode', country_col='Country'):
        for i, row in df[df[zip_col].isnull()].iterrows():
            city = row[city_col]
            country = row.get(country_col, 'US')
            zip_code = self.fetch_zip_code(city, country)
            if zip_code:
                df.at[i, zip_col] = zip_code
        return df


