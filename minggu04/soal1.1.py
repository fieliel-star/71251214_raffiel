userInput = input("Masukan suhu badan: ")
try: 
    suhu = int(userInput)
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
except:
    print ("Anda salah menginput nilai suhu badan. Nilai harus angka")