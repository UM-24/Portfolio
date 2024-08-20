#This script pulls IDs from a massive list and chunks them into groups of 900 (SQL Update Script limit is 1k)
import pandas as pd
import os as osc

csvfile = pd.read_csv(r"C:\Users\MyCSV File Path")
print(csvfile)

chunk_size = 900

def process_chunk(chunk):
return 'INSERT INTO A_Reg_Ids(ID) VALUES ' + ', '.join(f"({x})" for x in chunk) + ';'

def process_all(data, n):
return [process_chunk(data[i+n]['ID']) for i in range(0, len(data), n)]

insert = process_all(csvfile, chunk_size)
file_name = 'Name the Output File .csv/.txt etc'
file_path = osc.path.join(r"C:\Users\My Output Path", file_name)

for statement in insert:
print(statement)

with open(file_path, 'w') as f:
for statement in insert:
f.write(statement + "\n\n")