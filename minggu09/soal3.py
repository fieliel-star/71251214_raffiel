import re 

kalimat = str(input("masukan kalimat: ")).strip()

x = re.split(r"\s+", kalimat)
noSpace = ' '.join(x)

print(noSpace)