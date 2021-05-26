import os
cwd = os.getcwd()
path = os.path.join(cwd, "JSON_RAIN.py")

import csv
import json
import pandas as pd

with open('F:/fdrs_bmkg/data/GSMAP_20200405.csv', 'rb') as f_input, open('F:/fdrs_bmkg/data/GSMAP_20200405_decimal.csv', 'wb') as f_output:
    csv_input = csv.reader(f_input)
    csv_output = csv.writer(f_output)
    csv_output.writerow(next(csv_input))    # write header
    
##Merubah Angka Desimal
    for cols in csv_input:
        for i in xrange(2, 13):
            cols[i] = '{:.0f}'.format(float(cols[i]))
        csv_output.writerow(cols)

print("MENGGANTI NILAI DECIMAL")


df = pd.read_csv("F:/fdrs_bmkg/data/GSMAP_20200405_decimal.csv",sep=",",header=0,names=["lon","lat","FWI","FFMC","DMC","DC","ISI","BUI","DSR","T","RH","WIND","PREC"])
df.to_csv("F:/fdrs_bmkg/data/GSMAP_20200405_decimal.csv", index=False)
print(df.head)

file = 'F:/fdrs_bmkg/data/GSMAP_20200405_decimal.csv'
json_file = 'F:/fdrs_bmkg/data/GSMAP_20200405_FIX_1.json'
fieldnames = ("lon","lat","FWI","FFMC","DMC","DC","ISI","BUI","DSR","T","RH","WIND","PREC")

        
##Read CSV File
def read_CSV(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)
print("Membaca File CSV")
      
##Convert csv data into json
def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=10, separators=(',', ': '))) #for pretty
        f.write(json.dumps(data))
print("FINISH")


read_CSV(file,json_file)
