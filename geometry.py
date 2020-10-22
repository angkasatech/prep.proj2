from geometry.segitiga import hitung_luas_segitiga, infosegitiga
import geometry.segitiga as gs
from geometry.persegipanjang import hitung_luas_persegi, infopersegi as infop

print(f'hitung luas segitiga {hitung_luas_segitiga(13,5)}')

print('-------------')

print(f'\n{infosegitiga()}')
print(f'hitung luas segitiga {gs.hitung_luas_segitiga(13,7)}')

print('-------------')

print(f'\n{infop()}')
print(f'hitung luas persegi {hitung_luas_persegi(10,7)}')