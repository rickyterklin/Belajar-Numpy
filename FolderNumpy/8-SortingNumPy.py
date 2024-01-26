import numpy as np

"""
###  1
a = np.floor(np.random.randn(1,6)*10)

print(a)
print("nilai max dari a = ", a.max()) # mengetahui nilai terbesar dalam array
print("posisi max dari a = ", a.argmax()) # mengetahui posisi nilai terbesar
print("nilai min dari a = ", a.min()) # mengetahui nilai terkecil dalam array
print("posisi min dari a = ", a.argmin()) # mengetahui posisi nilai terkecil

# mengurutkan nilai a
print("mengurutkan nilai a")
print(np.sort(a))
print(np.argsort(a)) # mengurutkan dari array awal


###  2
a = np.floor(np.random.randn(2,2)*10)

print(a)
print("nilai max dari a = ", a.max()) # mengetahui nilai terbesar dalam array
print("posisi max dari a = ", a.argmax()) # mengetahui posisi nilai terbesar
print("nilai min dari a = ", a.min()) # mengetahui nilai terkecil dalam array
print("posisi min dari a = ", a.argmin()) # mengetahui posisi nilai terkecil

# mengurutkan nilai a
print("mengurutkan nilai a")
print(np.sort(a))
print(np.argsort(a)) # mengurutkan dari array awal (mengurutkan sesuai baris)
"""

###  3
dtipe = [('nama','S10'),('tinggi',int)]
data = [
    ('Zoro',178),
    ('Ananda',190),
    ('Roger',168)
]

a = np.array(data, dtype=dtipe)
print(a)

print(np.sort(a, order='tinggi'))
print(np.sort(a, order='nama'))