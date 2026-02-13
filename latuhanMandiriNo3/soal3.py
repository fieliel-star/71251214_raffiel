import math
modalAwal = 200000000
targetUang = 400000000
bungaPerTahun = 0.1
waktuYangDiButuhkan = math.log(targetUang / modalAwal) / math.log(1 + bungaPerTahun)
print ("Waktu yang dibutuhkan =", round(waktuYangDiButuhkan), "Tahun")