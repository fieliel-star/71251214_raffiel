file = open("soal.txt", "r")
print("nama file1: soal.txt")

for baris in file:
    bagian = baris.strip().split("||")
    soal = bagian[0].strip()
    kunci = bagian[1].strip()

    print(soal)
    
    jawab = input("Jawab: ")

    if jawab.strip().lower() == kunci.lower():
        print("Jawaban benar!")
    else:
        print("Jawaban salah!")
    
    print() 

file.close()