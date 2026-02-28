userInput = input("Masukan bulan (1-12): ")
try:
    bulan = int(userInput)
    if bulan in (1, 3, 5, 7, 8, 10, 12):
        print("Jumlah hari:",31,"hari")
    elif bulan in (4, 6, 9, 11):
        print("Jumlah hari:",30,"hari")
    elif bulan == 2:
        print("Jumlah hari:",29, "hari")
    else:
        print("Bulan tidak valid")
except:
    print ("Anda salah menginput nilai bulan. Ulang kembali!!")