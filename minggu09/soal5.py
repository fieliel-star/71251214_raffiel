import re
from datetime import datetime

def cari_dan_hitung_selisih(teks):
    list_tanggal = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', teks)
    sekarang = datetime.now()

    for tgl_str in list_tanggal: 
        tgl_obj = datetime.strptime(tgl_str, "%Y-%m-%d")
        selisih = (sekarang - tgl_obj).days
        print(f"{tgl_obj} selisih {selisih} hari")

teks = input("masukan teks: ")

cari_dan_hitung_selisih(teks)