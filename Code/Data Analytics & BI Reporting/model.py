# We can generate a EDA report using pandas-profiling libraries, which can give useful insights of the dataset within minutes.
# Beneficiary if we want to analyse a dataset for a quick overview
# pip install pandas
# pip install pandas-profiling

import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_excel('Practice-Data.xlsx')
print(df)

# Generate a EDA report
profile = ProfileReport(df)
profile.to_file(output_file="output-model.html")
