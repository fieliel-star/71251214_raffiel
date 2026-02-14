gajiPerjam = int(input("masukan gaji: "))
jamKerjaDalamSeminggu = int(input ("masukan jam kerja: "))

totalJam =  jamKerjaDalamSeminggu * 5
gajiKotor = gajiPerjam * totalJam
gajiSetelahPajak = gajiKotor - (gajiKotor * 0.14)
keperluan = gajiSetelahPajak * 0.10
alatTulis = gajiSetelahPajak * 0.01
sisaUang = gajiSetelahPajak - keperluan - alatTulis
sedekah = sisaUang * 0.25
yatim = sedekah * 0.30 
dhuafa = sedekah * 0.70

print("Gaji sebelum bayar pajak:", "Rp", round(gajiKotor, 2))
print("Gaji setelah bayar pajak:", "Rp", round(gajiSetelahPajak, 2))
print("Pakaian dan aksesoris:", "Rp", round(keperluan, 2))
print("Alat tulis:", "Rp", round(alatTulis, 2))
print("Sedekah:", "Rp", round(sedekah, 2))
print("Diterima anak yatim:", "Rp", round(yatim, 2))
print("Diterima kaum dhuafa:", "Rp", round(dhuafa, 2))