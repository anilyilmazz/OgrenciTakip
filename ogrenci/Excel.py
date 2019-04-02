import pandas
from ogrenci.forms import ogrenci_Ekle_form
from datetime import datetime

yol = r'C:\Users\yunus\Desktop\ogrenciler.xlsx'

data = pandas.read_excel(io=yol, sheet_name=0)  # , encoding='utf-8'
ogrenciler = []
for index in range(len(data)):
    ogrenciler.append(ogrenci_Ekle_form())

    ogrenciler[index].tc = data.iloc[index, 0]
    ogrenciler[index].adSoyad = data.iloc[index, 1]
    # tempDate = str(data.iloc[index, 2]).split(' ')[0].replace('-', '/')
    # tempDate = tempDate.split('/')[2] + '/' + tempDate.split('/')[1] + '/' + tempDate.split('/')[0]
    # ogrenciler[index].dogum_tarihi = tempDate
    ogrenciler[index].tel = data.iloc[index, 3]
    ogrenciler[index].aolNo = data.iloc[index, 4]
    ogrenciler[index].veli_ad = data.iloc[index, 5]
    ogrenciler[index].veli_tel = data.iloc[index, 6]
    ogrenciler[index].adres = data.iloc[index, 7]
