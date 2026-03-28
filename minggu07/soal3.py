tinggi = int(input("Tinggi: "))
lebar = int(input("Lebar: "))

angka = 1
for i in range(tinggi):
    for j in range(lebar):
        print(angka, end=" ")
        angka += 1
    print()