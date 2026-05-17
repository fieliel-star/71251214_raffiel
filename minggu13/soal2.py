def bio(data):
    print("NIM :", data[1])
    print("NAMA :", data[0])
    print("ALAMAT :", data[2])

    nim = tuple(data[1])
    print("NIM:", nim)

    namaDepan = tuple(data[0].split()[0].lower())
    print("NAMA DEPAN:", namaDepan)

    namaBelakang = data[0].split()[0:]
    namaBelakang.reverse()
    namaBelakang = tuple(namaBelakang)
    print("NAMA TERBALIK:", namaBelakang)

data = ("Raffiel Gideon Nyolo Nyolo", "71251214", "Buyumpondoli")
bio(data)