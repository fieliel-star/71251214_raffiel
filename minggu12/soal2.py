lista = ['red', 'green', 'blue']
listb = ['#FF0000','#008000', '#0000FF']

hasil = {}
for lista, listb in zip(lista, listb):
    hasil[lista] = listb
    
print(hasil)