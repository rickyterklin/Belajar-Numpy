import numpy as np

## membuat Matrix dengan type data tertentu
a = np.array(([1,2,3],[4,5,6]), dtype = float)

## membuat array dengan menggunakan Function
def kuadrat(baris,kolom):
    return kolom**2
def jumlah(baris,kolom):
    return kolom + baris


# b = np.fromfunction(FUNGSI, (UKURAN MATRIX), TIPE DATA)  ## contoh
b = np.fromfunction(kuadrat, (1,10), dtype=int)  ## penggunaan
c = np.fromfunction(jumlah, (4,5), dtype=int)  ## penggunaan

print(c,"\n")

## membuat array atau matrix dengan menggunakan Iterable
iterable = (x*2 for x in range(5))
d = np.fromiter(iterable, dtype=int)
print(d,"\n")

# multitype array data custom
dtipe = [('nama','S255'),('tinggi',int)]
data = [('sanji',150),
         ('zoro',167),
         ('shanks',177)]

e = np.array(data, dtype=dtipe)

print(e[1])