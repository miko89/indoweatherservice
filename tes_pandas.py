import pandas as pd

df = pd.read_csv("F:/fdrs_bmkg/data/info.csv",sep=",",header=0,names=["Lintang","Bujur","Tanggal","Waktu Akuisisi","Tingkat Kepercayaan","Satelit","Kecamatan","Kabupaten","Provinsi"])
df.to_csv("F:/fdrs_bmkg/data/info_ubah.csv", index=False)
print(df.head())
