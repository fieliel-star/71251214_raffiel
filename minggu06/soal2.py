def ganjil(bawah, atas):
    if bawah < atas:
        for i in range(bawah, atas + 1):
            if i % 2 != 0:
                if i + 2 <= atas:
                    print(i, end=", ")
                else:
                    print(i, end="")
    else:
        for i in range(bawah, atas - 1, -1):
            if i % 2 != 0:
                if i - 2 >= atas:
                    print(i, end=", ")
                else:
                    print(i, end="")

bawah = int(input("Bawah = "))
atas = int(input("Atas = "))

ganjil(bawah, atas)