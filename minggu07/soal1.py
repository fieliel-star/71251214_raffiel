n = int(input("Masukan bilangan: "))

if n <= 2:
    print("Tidak ada bilangan prima kurang dari n")
else:
    for i in range(n-1, 1, -1):
        prima = True
        for j in range(2, i):
            if i % j == 0:
                prima = False
                break
        if prima:
            print(f"Bilangan prima terdekat dan kurang dari {n} adalah {i}")
            break