beratBadan = float(input("Masukan berat badan: "))
tinggi = float(input("Masukan tinggi badan: "))

tinggi = tinggi / 100
BMI = beratBadan / tinggi**2

print (round (BMI,2))