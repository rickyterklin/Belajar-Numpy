import numpy as np

a = np.array(([1,2,3],
              [4,5,6],))

print("Matrix a dengan ukuran : ", a.shape)
print(a)

## Transpose Matrix (Merubah dari baris menjadi kolom begitu juga sebaliknya)
# catatan Transpose tidak merubah nilai dari a
print("Transpose Matrix a :")
print(a.transpose()) # Cara 1 untuk transpose
print(np.transpose(a)) # Cara 2 untuk transpose
print(a.T) # Cara 3 untuk transpose



## Flatten Array , Vector Baris ( Merubah vector menjadi 1 baris)
print("Flatten Matrix a :")
print(a.ravel())
print(np.ravel(a))

## Reshape Matrix
# merubah bentuk matrix dan diurutkan sesuai reshape
# berbeda dengan transpose yg pindah kolom dan baris
print("Reshape Matrix a:")
print(a.reshape(3,2))
print(a.reshape(6,1))

## Resize Matrix
# merubah bentuk matrix sesuai resize tapi bedanya yg berubah nilai a
# berbeda dengan reshape bukan nilai yg berubah
print("Resize Matrix a:")
a.resize(3,2)
print(a)
print("Matrix a dengan ukuran : ", a.shape)