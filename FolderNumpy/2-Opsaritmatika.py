import numpy as np

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array Numpy
anp = np.array([1,2,3,4,5,])
bnp = np.array([6,7,8,9,10,])

# penjumlahan( akan ditambahkan kedalam list bukan elemetnya)
# tidak bisa menggunakan operasi - , * , /
hasil = a+b
print(hasil)

# Element wise Operation ( akan ditambahkan perelement)
# jumlah element harus sama 
hasil1 = anp + bnp

# pengurangan
# akan tidak berfungsi
hasil2 = anp - bnp

# perkalian
hasil3 = anp * bnp

# pembagian
hasil4 = anp / bnp

# kuadrat
hasil5 = anp**2
print(hasil5)


# multidimensi array Numpy
c = np.array([(1,2,3),(4,5,6)])
d = np.array([(7,8,9),(-1,-2,-3)])

hasil6 = c + d
hasil6 = c * d # perkalian dalam matrix tetap mengalikan perelement( u/ perkalian matrix beda lagi)
print(hasil6)