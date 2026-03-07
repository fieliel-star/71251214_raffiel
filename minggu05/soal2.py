def cek_digit_belakang(a,b,c):
    if a % 10 == b % 10 or b % 10 == c % 10 or a % 10 == c % 10: 
        return True
    else:
        return False

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

print(cek_digit_belakang(a,b,c))