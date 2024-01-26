## Indexing, Slicing dan Iterasi

import numpy as np

a = np.arange(10)**2

print(a)

# mengambil nilai

print('mengambil elemen ke-1', a[0])
print('mengambil elemen ke-5', a[5])
print('mengambil elemen akhir', a[-1]) ## gunakan a[-1]) untuk mengambil nilai terakhir

# Slicing
print('mengambil elemen dari 0-6', a[0:5]) # start-end (index dimulai dari 0) jadi nilai akhir -1
print('mengambil elemen dari 3-akhir', a[2:])
print('mengambil elemen dari awal-5', a[:5])

# Iterasi
for i in a:
    print('value = ',i)
