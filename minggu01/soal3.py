import math
modalAwal = 200_000_000
targetUang = 400_000_000
bungaPerTahun = 0.1
phi = math.pi
waktuYangDiButuhkan = math.log(targetUang / modalAwal) / math.log(1 + bungaPerTahun)
print ("Waktu yang dibutuhkan =", round(waktuYangDiButuhkan), "Tahun")
print (phi)