def perkalian(a, b):
    hasil = 0
    proses = ""

    for i in range(a):
        hasil += b
        proses += str(b)
        if i < a - 1:
            proses += " + "
    print(f"{a} x {b} = {proses} = {hasil}")

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
perkalian(angka1, angka2)