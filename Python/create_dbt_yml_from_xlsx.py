#This mass creates YML files pulling from an excel sheet, it creates 8 rows per row in excel. Need to manually type models: in at the beginning of the finished YML file to avoid duplication
import pandas as pd

excel = r"My Excel File Path" #replace with your excel file path
df = pd.read_excel(excel, sheet_name='Sheet 1') #replace with the name of the sheet you want it too look at

template = """

name: {file}
description:
columns:
name: {skname}
description: Primary key. Hashed composite of unique id and db_id.
data_tests:
unique
not_null"""

output = r"My output path" #replace with the file output destination

with open(output, "w") as f:
for index, row in df.iterrows():
file = row['FileName'] #replace with the excel column name that contains what you want to name the file
skname = row['sk'] #replace with the excel column name that contains the _sk name
model = template.format(file=file, skname=skname)
f.write(model)