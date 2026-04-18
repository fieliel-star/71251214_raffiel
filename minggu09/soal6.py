import re
import random
import string

def generate_password(panjang=8):
    karakter = string.ascii_letters + string.digits
    return ''.join(random.choice(karakter) for _ in range(panjang))

def cari_email(teks):
    list_email = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', teks)

    for email in list_email:
        username = email.split("@")[0]
        password = generate_password(8)
        print(f"{email} username: {username} , password: {password}")

teks = input("Masukkan teks: ")
cari_email(teks)

