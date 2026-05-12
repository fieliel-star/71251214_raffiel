fname = input("Masukkan nama file : ")

try:
    fhand = open(fname)
except:
    print('file error tidak dapat dibuka:', fname)
    exit()

counts = {}
for line in fhand:
    if line.startswith('From '):
        email = line.split()[1]
        counts[email] = counts.get(email, 0) + 1

print(f"{email}: {counts}")