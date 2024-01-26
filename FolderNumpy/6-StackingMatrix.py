import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

## untuk perkalian jumlah baris & kolum mempengaruhi
## contoh jika jumlah kolum saat vstack tidak sesuai maka program tidak berjalan
aMat = np.ones((2,3))
bMat = np.zeros((2,3))

# Stacking Matrix / Menumpuk Matrix
# hstack untuk melanjutkan baris / vstack untuk menambah dibawahnya
c = np.hstack((a,b))
d = np.vstack((a,b))

cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat))

print(c)
print(d)
print(cMat)
print(dMat)