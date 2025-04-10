
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