def konversi_waktu(jam, menit, format_24):

    if (jam >= 24 or menit > 59 or jam < 0 or menit < 0):
        return "Opo iki"
        
    if format_24 == True:
         return "Jam : "+f"{jam:02d}:{menit:02d}"
    else:
        if jam == 0:
            konversi = 12
            waktu = "AM"
        elif jam < 12:
            konversi = jam
            waktu = "AM"
        elif jam == 12:
            konversi = 12
            waktu = "PM"
        else:
            konversi = jam - 12
            waktu = "PM"

        return "Jam : "+f"{konversi:02d}:{menit:02d} {waktu}"
        
#Jangan dirubah
if __name__ == "__main__":
    jam = int(input())
    menit = int(input())
    format = input()
    fformat = True if format == "true" else False
    print(konversi_waktu(jam,menit,fformat))