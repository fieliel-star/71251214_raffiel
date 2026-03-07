def konversi_suhu(celcius):
    c_ke_f = lambda c: (9/5) * c + 32
    c_ke_r = lambda c: 0.8 * c

    fahrenheit = c_ke_f(celcius)
    reamur = c_ke_r(celcius)
    return fahrenheit, reamur

celcius = float(input("Masukkan suhu dalam Celcius: "))
f, r = konversi_suhu(celcius)

print("Suhu dalam Fahrenheit:", int(f))
print("Suhu dalam Reamur:", int(r))