#buatlah sebuah program kasir yang menggunakan fungsi append pada list
#disertai di dalammnya terdapat fungsi while loop
#dan juga menggunakan kondisi if elif else

total = 0 
barang = []
harga = []

while True:
    print('''Daftar Barang : \n
    1.jilbab t\ 70000
    2.mukenah t\ 200000
    3.pasminah t\ 80000''')

    kode = int(input("masukkan kode barang :"))
    if kode == 1:
        barang.append("jilbab")
        harga.append('70000')
        total +=70000
    elif kode == 2:
        barang.append("mukenah")
        harga.append('200000')
        total +=200000
    elif kode == 3:
        barang.append("pasminah")
        harga.append('80000')
        total +=80000 
    else:
        print("kode yang Anda masukkan tidak valid")


lanjut = input("lanjut belanja y\t :")
if lanjut == "t":
    print("")
    break

print("barang yang dibeli:",barang)
print("harga barang: Rp",harga)
print("total harga semua barang: Rp",total)

uang = int(input("masukkan uang pembayaran: Rp"))
if uang > total:
    print("kembaliannya :",uang-total)
elif uang == total:
    print("uang pas")
else:
    print("uangnya kurang",uang-total)