file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

baris1 = file1.readlines()
baris2 = file2.readlines()

file1.close()
file2.close()

max_baris = max(len(baris1), len(baris2))

for i in range(max_baris):
    teks1 = baris1[i].strip() if i < len(baris1) else "<Tidak ada>"
    teks2 = baris2[i].strip() if i < len(baris2) else "<Tidak ada>"

    if teks1 != teks2:
        print(f"Perbedaan di baris {i+1}:")
        print(f"File 1: {teks1}")
        print(f"File 2: {teks2}")
        print("==============================")