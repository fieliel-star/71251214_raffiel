total = 0
count = 0

while True:
    user_input = input("Masukkan bilangan: ")
    
    if user_input.lower() == "done":
        break
    
    try:
        angka = float(user_input)
        total += angka
        count += 1
    except:
        print("Input tidak valid, masukkan angka atau 'done'.")

if count > 0:
    rata_rata = total / count
    print("Rata-rata:", rata_rata)
else:
    print("Tidak ada bilangan yang dimasukkan.")