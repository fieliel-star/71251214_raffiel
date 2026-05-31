n = int(input("Masukkan jumlah kategori: "))

if n <= 2:
    print("Jumlah kategori harus lebih dari 2.")
else:
    data_aplikasi = {}
    kategori_pertama = None

    for i in range(n):
        nama_kategori = input(f'Masukkan nama kategori ke-{i+1}: ')
        print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
        aplikasi = []
        for j in range(5):
            nama_aplikasi = input(f'Nama aplikasi {nama_kategori} ke-{j+1}: ')
            aplikasi.append(nama_aplikasi)
        if i == 0:
            kategori_pertama = nama_kategori
        else:
            data_aplikasi[nama_kategori] = []
        data_aplikasi[nama_kategori] = aplikasi

    print(f"Hasil --> {kategori_pertama} : {data_aplikasi[kategori_pertama]}  <--\n")