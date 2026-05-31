def cek_kata_sama(txt1, txt2):
    try:
        with open(txt1, 'r') as file1, open(txt2, 'r') as file2:
            kata1 = set(file1.read().lower().split())
            kata2 = set(file2.read().lower().split())
        
    except:
        print(f"Error: File tidak ditemukan, Coba kembali.")
        return
    
    kata_sama = list(kata1.intersection(kata2))
    
    if kata_sama:
        print("Kata-kata yang sama di kedua file:")
        print(kata_sama)
    else:
        print("Tidak ada kata yang sama di kedua file.")

    jumlah_kata_sama = len(kata_sama)
    return jumlah_kata_sama

txt1 = input("Masukkan nama file pertama: ")
txt2 = input("Masukkan nama file kedua: ")

jumlah_kata = cek_kata_sama(txt1, txt2)
if jumlah_kata is not None:
    print(f"(Jumlah kata yang sama di kedua file adalah: {jumlah_kata})\n")