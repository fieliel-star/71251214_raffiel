import re

kalimat = str(input("masukan kalimat: "))
cari =  str(input("masukan kata yang akan dicari: "))

kalimat = kalimat.lower()
cari = cari.lower()
kalimat = kalimat.replace(".", "")

x = re.split(r"\s", kalimat)
jumlah = x.count(cari)

print(f"{cari} ada {jumlah} buah")