userInputA = input("Masukkan sisi 1: ")
userInputB = input("Masukkan sisi 2: ")
userInputC = input("Masukkan sisi 3: ")
try:
    sisi1 = int(userInputA)
    sisi2 = int(userInputB)
    sisi3 = int(userInputC)
    if sisi1 == sisi2 == sisi2 == sisi3 :
        print ("3 sisi sama")
    elif sisi1 == sisi2 or sisi2 == sisi3 or sisi3 == sisi1:
        print ("2 sisi sama")
    else:
        print ("Tidak ada yang sama") 

except:
    print ("Anda salah menginput nilai bilangan")