def pembayaran():
    print("\n===========================================")
    nama = input("\n\tmasukan nama = ")
    nim = input("\tMasukan nim = ")
    semester=input("\tmasukan semester saat ini = ")
    print("\n\t---pilihan pembayaran---")
    print("\t1. pembayaran spp")
    print("\t2. pembayaran Semester pendek")
    pilih = input("\n\tsilahkan pilih : ")
    if pilih == "1":
        spp()
    elif pilih == "2":
        sp()
    else:
        exit
        tanya()
def spp():
    semester =int(input("\n\tjumlah semester yang di bayar = "))
    semester = float(semester)
    total = 500000*semester
    print("=====================================================")
    print("\ttotal bayar spp Rp.350000 *", semester," = Rp.",total)

def sp():
    sks = int(input("\n\tjumlah sks semester pendek = "))
    sks = float(sks)
    byr_sp = 25000*sks
    print("=====================================================")
    print("\ttotal bayar semesterpendek Rp.25000 *",sks," = Rp.",byr_sp)
