print('Welcome to Analyse Data!')
import pandas as pd
# the path to my excel file
file_path = 'data_glotip.csv'
# function to find (because i told it to) and read the data in the excel spreadsheet
data = pd.read_csv(file_path)
print(data.head())
