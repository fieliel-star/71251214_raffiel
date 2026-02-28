userInputA = input("Masukkan bilangan pertama: ")
userInputB = input("Masukkan bilangan kedua: ")
userInputC = input("Masukkan bilangan ketiga: ")
try:
    a = int(userInputA)
    b = int(userInputB)
    c = int(userInputC)
    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)
except:
    print ("Anda salah menginput nilai bilangan")