def cek_angka(a,b,c):
    if (a != b and b != c and a != c) and (a + b == c or b + c == a or a + c == b):
        return True
    else:
        return False

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

print(cek_angka(a,b,c))