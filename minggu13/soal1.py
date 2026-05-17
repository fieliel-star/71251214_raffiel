def tup(tA):
    for i in tA :
        if i != tA[0]:
            return False
    return True

tA = (90,90,90,90)
print(tup(tA))