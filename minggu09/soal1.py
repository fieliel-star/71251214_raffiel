inpUser1 = input("masukan kata pertama: ")
inpUser2 = input("masukan kata kedua: ")

kata1 = ''.join([i.lower() for i in inpUser1 if i.isalpha()])
kata2 = ''.join([i.lower() for i in inpUser2 if i.isalpha()])

if sorted(kata1) == sorted(kata2):
    print("anagram")
else:
    print("bukan")