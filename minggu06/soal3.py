def ips(x):
    qwe = 0    
    for i in range(1,x+1):
        nilai = str(input(f"Nilai MK {i}: "))
        if nilai == "A":
            qwe += 4
        elif nilai == "B":
            qwe += 3
        elif nilai == "C":
            qwe += 2
        elif nilai == "D":
            qwe += 1
        else:
            qwe += 0
    qwe = qwe / x
    return f"Nilai IPS anda semester ini {qwe:.2f}"

print("Program penghitung IPS Mahasiswa")
x = int(input("Berapa jumlah mata kuliah? "))
print(ips(x))