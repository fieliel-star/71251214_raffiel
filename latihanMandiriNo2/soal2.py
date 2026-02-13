berat_awal = 25
harga_awal = 650000
harga_naik = 685000
modal_awal = berat_awal * harga_awal
keuntungan = (berat_awal * harga_naik) - modal_awal

persen_keuntungan = (keuntungan / modal_awal) * 100

berat_akhir = 15
harga_akhir = 685000
harga_sekarang = 715000
total_berat = berat_awal + berat_akhir
total_modal = modal_awal + (berat_akhir * harga_akhir)
nilai_sekarang = total_berat * harga_sekarang
keuntungan2 = nilai_sekarang - total_modal

persen_keuntungan2 = (keuntungan2 / total_modal) * 100

print("Modal awal:" "Rp",modal_awal)
print("Keuntungan awal:" "Rp",keuntungan)
print("Persentase keuntungan awal:",  round (persen_keuntungan),"%")

print("Total modal:" "Rp",total_modal)
print("Keuntungan sekarang:" "Rp",keuntungan2)
print("Persentase keuntungan sekarang:",  round (persen_keuntungan2),"%")