import os
cwd = os.getcwd()
path = os.path.join(cwd, "hotspot_oke.py")

import csv
import json
import pandas as pd
import pandas as pd


# df = pd.read_csv("F:/fdrs_bmkg/data/hotspot_20200727.txt",sep="/t", engine='python',header=0,names=["BUJUR", "LINTANG", "KEPERCAYAAN", "REGION", "PROVINSI", "KABUPATEN", "KECAMATAN","SATELIT", "TANGGAL", "WAKTU"])
# df.to_csv("F:/fdrs_bmkg/data/hotspot_20200727.csv", index=False)
# print(df.head)

file = 'F:/fdrs_bmkg/data/data_siklon_18utc.csv'
json_file = 'F:/fdrs_bmkg/data/data_siklon_seroja_18.json'
fieldnames = ("Time","Latitude","Longitude","Symbol","Category","Pressure","MeanWind","WindGust")

        
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
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))) 
print("FINISH")


read_CSV(file,json_file)
