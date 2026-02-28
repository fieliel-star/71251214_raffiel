userInput = input("Masukan bilangan: ")
try:
    bilangan = int(userInput)
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")
except:
    print ("Anda salah menginput nilai bilangan")