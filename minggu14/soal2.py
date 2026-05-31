def tampilkan_konversi(asli, terkonversi):
    print(f"Data sebelum konversi:{asli}",type(asli))
    print(f"Data setelah konversi:{terkonversi}",type(terkonversi))
    print()

def list_ke_set(data_list):
    set_data = set(data_list)
    tampilkan_konversi(data_list, set_data)
    return set_data

def set_ke_list(data_set):
    list_data = list(data_set)
    tampilkan_konversi(data_set, list_data)
    return list_data

def tuple_ke_set(data_tuple):
    set_data = set(data_tuple)
    tampilkan_konversi(data_tuple, set_data)
    return set_data

def set_ke_tuple(data_set):
    tuple_data = tuple(data_set)
    tampilkan_konversi(data_set, tuple_data)
    return tuple_data

data_list   = [1, 2, 3, 4, 5]
data_set    = {5, 6, 7, 8, 9}
data_tuple  = (10, 11, 12, 13, 14)

hasil_set   = list_ke_set(data_list)
hasil_list  = set_ke_list(data_set)
hasil_set2  = tuple_ke_set(data_tuple)
hasil_tuple = set_ke_tuple(data_set)