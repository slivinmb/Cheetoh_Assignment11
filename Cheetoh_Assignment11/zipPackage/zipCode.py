# File Name : zipCode.py
# Student Name: Michael Slivinski and Will Claus
# email: slivinmb@mail.uc.edu, clausws@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment shows us how to connect to an api and add zip codes to a csv file.

# Brief Description of what this module does: This module shows the zip codes that need to be added
# Citations: 

# Anything else that's relevant:

import re
import requests

class ZipCodeFiller:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://app.zipcodebase.com/api/v1/code/city"

    def has_zip_code(self, address):
        """Check if a 5-digit ZIP code already exists in the address."""
        return bool(re.search(r"\b\d{5}\b", address))

    def extract_city(self, address):
        """Extract the city (assumed to be second-to-last part of comma-separated address)."""
        parts = [part.strip() for part in address.split(',')]
        if len(parts) >= 2:
            return parts[-2]
        return None

    def fetch_zip_code(self, city, country="us"):
        """Call Zipcodebase API with city and state (always 'Ohio') using API key in URL."""
        url = f"{self.base_url}?apikey={self.api_key}&city={city}&state_name=Ohio&country={country}"

        try:
            response = requests.get(url)
            print(f" Request: {url}")
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                if results:
                    zip_code = results[0]
                    print(f" ZIP for {city}, Ohio: {zip_code}")
                    return zip_code
                else:
                    print(f" No ZIP found in results for: {city}")
            else:
                print(f" API error {response.status_code}: {response.text}")
        except Exception as e:
            print(f" Exception during API call for {city}: {e}")
        return None

    def fill_missing_zip_codes(self, df, address_col='Full Address', max_updates=5):
        """Append ZIP codes to the first N addresses missing them."""
        updated = 0
        for i, row in df.iterrows():
            if updated >= max_updates:
                break

            address = row[address_col]
            if self.has_zip_code(address):
                continue

            city = self.extract_city(address)
            if not city:
                print(f" Could not extract city from: {address}")
                continue

            zip_code = self.fetch_zip_code(city)
            if zip_code:
                df.at[i, address_col] = f"{address.strip()} {zip_code}"
                updated += 1
                print(f" Appended ZIP {zip_code} to: {address}")
            else:
                print(f" No ZIP added for: {address}")
        print(f" Total updated addresses: {updated}")
        return df

         

       


