# This pulls from an excel file that i have mass created SQL queries from that reside in Column 2 and mass generates sql files
import pandas as pd
import os as osc

excel = r"C:\Users\My Excel Path" #remame to the path where your excel file lives
df = pd.read_excel(excel,sheet_name='Sheet 1') #rename to the tab of your final data

for index, row in df.iterrows():
table = row['Column Name'] #this pulls the table name (from a column in the excel file) for the file naming
query = row['Column Name2'] #this pulls the script for the actual file contents
file_name = f"stg_database__{table}.sql" #this is the output sql file name which uses text + the text value from the table variable
file_path = osc.path.join(r"C:\Users\My Output Path", file_name) #rename to your output file path

with open(file_path, "w") as f:
    f.write(query)