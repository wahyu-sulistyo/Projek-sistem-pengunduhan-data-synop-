# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:40:50 2020

@author: Asus
"""

#downloads data cuaca pada web ogimet
#import modul modul yang digunakan terlebih dahulu
import wget
from termcolor import colored
#Nama Program pengunduhan
print (colored("PROGRAM PENGUNDUHAN DATA SYNOP",'blue',attrs=['bold']))

chunk_size = 1024
#lokasi website untuk download data

# website laman ogimet
url = "http://www.ogimet.com/cgi-bin/getsynop?block=123&"
print (colored ('A.silahkan input tanggal awal dan tanggal akhir data synop yang ingin diunduh','yellow',attrs=['bold']))
print ('CONTOH input =200912010000 (tahun|bulan|tanggal|jam) ')


#atur tanggal awal data yang diinginkan
print (colored('1.input tahun|bulan|tanggal|jam waktu awal data yang akan diunduh','green',attrs=['bold']))
tanggalawal = str (input("masukkan tanggal awal data yang diinginkan :"))

#atur tanggal akhir data yang diinginkan
print (colored('2.input tahun|bulan|tanggal|jam waktu akhir data yang akan diunduh','green',attrs=['bold']))
tanggalakhir = str (input("masukkan tanggal akhir data yang diinginkan :"))

#lokasi penyimpanan data
path = "D:/projek UAS/download data cuaca/dataprojek.csv"

url_lengkap = url + "begin=" + tanggalawal + "&" + "end=" + tanggalakhir + "&lang=eng&state=ind" 
print (colored(url_lengkap,'yellow',attrs=['bold']))



print (colored("B.periksa input url anda terlebih dahulu","red",attrs=['bold']))
print ('C.ketik y apabila input url telah sesuai')
print("y/n", end=': ')

answer = input()

while True:
    if answer == 'y':
        print (colored("D.silahkan beri nama pada data yang ingin anda unduh","yellow",attrs=["bold"]))
        storage = "D:/projek UAS/download data cuaca/"
        Nama_Data = str (input("ketik nama data yang ingin disimpan :"))
        Path = storage + Nama_Data + ".csv" 
        print (colored("......data sedang dalam proses download melalui web ogimet.....","blue",attrs=['bold']))
        wget.download(url_lengkap, Path)
        break
    elif answer == 'n':
        
        print("That is not a valid answer, please answer with y/n.")
        answer = input()
        break

print(colored("DOWNLOAD SELESAI","yellow",attrs=['underline']))
print(colored('selamat anda berhasil mengunduh data dari web ogimet.',attrs=['bold']))
