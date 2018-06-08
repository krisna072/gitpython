import texttable as tt
from perhitungan.penilaian import nilai_mahasiswa
from perhitungan.pembayaran import pembayaran
from perhitungan.calculator import pilihan

def menu():
    print("==========================================")
    print("\n\t----pilihan---")
    print("\t1. penilaian mahasiswa")
    print("\t2. pembayaran mahasiswa")
    print("\t3. calculator")
    
    pilih=input("\n\tsilakan pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2":
        pembayaran()
    elif pilih == "3":
        pilihan()
    else:
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke menu utama(y/n)?")
    if tanya == "y":
        menu()
    elif tanya == "n":
        exit
    else:
        print ("\n\tSalah input................!!!")
username=input("\nUsername : ")
password=input("\nPassword : ")
print("======================================================")
if username == "tommy" and password == "rahasiya":
    menu()

else:
    print("maaf password salah...!!!")

    
          
