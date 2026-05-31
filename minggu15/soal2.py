def cek_palindrom(nilai):

    nilai_str = str(nilai)

    if len(nilai_str) <= 1:
        return True
    else:
        return nilai_str[0] == nilai_str[-1] and cek_palindrom(nilai_str[1:-1])


try:
    nilai = int(input("Masukkan bilangan:"))  
    if cek_palindrom(nilai):  
        print("Nilai ini merupakan bilangan palindrom!")  
    else:  
        print("Nilai ini bukan merupakan bilangan palindrom!")  
except :
    print("Input yang dimasukkan bukan angka")