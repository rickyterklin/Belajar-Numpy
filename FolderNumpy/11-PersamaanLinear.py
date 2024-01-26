import numpy as np

a = np.array([(2,3),(1,2)])
y = np.array([23,14])
print(a)
print(y)

a_inv = np.linalg.inv(a)
# menyelsaikan persamaan linier
x = np.dot(a_inv,y)
print(x)

# cara lain
x2 = np.linalg.solve(a,y)
print(x2)