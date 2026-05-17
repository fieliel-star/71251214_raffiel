fname = input("Masukkan nama file : ")
try:
    fhand = open(fname)
except:
    print('file error tidak dapat dibuka:', fname)
    exit()

counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(":")[0]
        counts[time] = counts.get(time, 0) + 1

jam = sorted(counts.items())
for kunci, nilai in jam:
    print(f"{kunci} {nilai}")