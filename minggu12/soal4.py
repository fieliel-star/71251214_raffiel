def hitung_email(nama_file):
    email = {}
    try:
        with open(nama_file, 'r') as file:
            for line in file:
                if line.startswith('From '):
                    domain = line.split()[1].split('@')[1]
                    email[domain] = email.get(domain, 0) + 1
    except FileNotFoundError:
        print('file error tidak dapat dibuka:',email)
    return email

def main():
    fname = input("Masukkan nama file : ")
    email = hitung_email(fname)
    print(email)

if __name__ == "__main__":
    main()