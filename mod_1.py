"""
Program menghitung luas segitiga
luas segitiga = alas * tinggi / 2
"""
print('menghitung luas segitiga1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('menghitung luas segitiga 1 dengan banyak soal tanpa copas')
alas = 20
tinggi = 5
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas={luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 5)}')

#other option
alas=10
tinggi=6
print(f'\nSegitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas= {hitung_luas_segitiga(alas, tinggi)}')