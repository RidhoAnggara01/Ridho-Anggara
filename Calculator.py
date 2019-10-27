import os

os.system("clear")
print ("""\033[30;1m[•]=======================================[•]
\033[31;1m|#               Welcome to Tools Calculator        #|
\033[32;1m|# Author    : MR_CYBER_DHO                            #|
\033[33;1m|# Contact   : 089661363050                #|
\033[34;1m|# GitHub     : https://github.com/RidhoAnggara01         #|
\033[35;1m|# InstaGram  : ridho_anggara01            #|
\033[36;1m|# NOTES!!!  : Lapor ke MR_CYBER_DHO Bila Ada Tools Yang Error #|
\033[37;1m|# Donasi pulsa : 089661363050 [Yang Baik Hati]    #|
\033[30;1m[•]=================================================[•]""")

''' Program kalkulator sederhana untuk menjumlah, mengurang, mengkali, dan membagi bilangan dengan menggunakan fungsi '''
import sys , os

# fungsi penjumlahan
def add(x, y):
   return x + y
# fungsi pengurangan
def subtract(x, y):
   return x - y
# fungsi perkalian
def multiply(x, y):
   return x * y
# fungsi pembagian
def divide(x, y):
   return x / y
# menu operasi
os.system("clear")
os.system("figlet xNot_Found | lolcat")
print("\033[1;31;1m")
print("========Pilih Operasi=======")
print("1.Penjumlahan")
print("2.Pengurangan")
print("3.Perkalian")
print("4.Pembagian")
# Meminta input dari user
choice = input("Masukkan pilihan(1/2/3/4): ")
num1 = int(input("Masukkan bilangan pertama: "))
num2 = int(input("Masukkan bilangan kedua: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   os.system("figlet Mohon Maaf | lolcst")
   print("Sepertinya Format Yang Anda Masukkan Salah")	
   print("Please Wait A Second")
   os.system("sleep 3"		
	os.system("python2 calculator.py")
