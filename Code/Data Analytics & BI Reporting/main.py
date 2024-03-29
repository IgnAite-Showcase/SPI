# Internship Practice Model
# This python model is made by using pandas functionalities, where we can import any kind of dataset like csv, xlsx etc.
# And can perform data processing operations and basic cleaning of the data.

import pandas as pd

class Data:
    def __init__(self, i_file, o_file):
        self.data = None
        self.i_file = i_file
        self.o_file = o_file

    def import_data(self):
        try:
            # Load data from CSV file
            self.data = pd.read_excel(self.i_file)
            print("Data imported successfully.")

        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print("An error occurred while loading the data:", e)

    def clean_data(self):
        try:
            # Remove duplicate rows
            self.data = self.data.drop_duplicates()

            # Keep only rows where `Column_Name` is greater than 0
            self.data = self.data[self.data['Discount'] > 0]

            # Drop columns with NA values
            self.data = self.data.dropna()
            print("Data cleaned successfully.")

        except Exception as e:
            print("An error occurred while cleaning the data:", e)

    def processing_data(self):
        try:
            # Perform data processing and transformation operations
            # Modify a column into a new column
            self.data['Updated Quantity'] = self.data['Quantity'] * 2
            print("Data processed successfully.")

        except Exception as e:
            print("An error occurred while processing the data:", e)

    def export_data(self):
        try:
            # Save the processed data to CSV or Excel file
            self.data.to_excel(self.o_file, index=False)
            print("Processed data saved to", self.o_file)

        except Exception as e:
            print("An error occurred while saving the data:", e)


# Initialise the file names
i_file = 'Practice-Data.xlsx'
o_file = 'Sample-output-data.xlsx'

# Call the functions that are declared above
model = Data(i_file, o_file)
model.import_data()
model.clean_data()
model.processing_data()
model.export_data()

