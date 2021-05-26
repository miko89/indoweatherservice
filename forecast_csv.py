import os
cwd = os.getcwd()
path = os.path.join(cwd, "forecast_csv.py")

import csv
import json
import pandas as pd

##df = pd.read_csv("F:/spartan_pdc/data/Prakiraan_Cuaca_Cikarang.csv",sep=";",header=0,names=["ID","WAKTU","RH","SUHU","CUACA","ARAH","KECEPATAN"])
##df.to_csv("F:/spartan_pdc/data/OKE.csv", index=False)
##print(df.head)

file = 'F:/spartan_pdc/data/Prakiraan_Cuaca_Cikarang.csv'
json_file = 'F:/spartan_pdc/data/forecast.json'
fieldnames = ("ID","WAKTU","RH","SUHU","CUACA","ARAH","KECEPATAN")

        
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
        f.write(json.dumps(data, sort_keys=False, indent=7, separators=(',', ': '))) #for pretty
        f.write(json.dumps(data))
print("FINISH")


read_CSV(file,json_file)
