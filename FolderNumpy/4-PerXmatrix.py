import numpy as np

a = np.array(([1,2],
              [3,4]))
b = np.ones([2,2])

print("Matrix a =")
print(a)

print("Matrix b =")
print(b)

# perkalian matrix
cara1 = np.dot(a,b)
cara2 = a.dot(b)

print("Matrix cara1 =")
print(cara1)

print("Matrix cara2 =")
print(cara2)

