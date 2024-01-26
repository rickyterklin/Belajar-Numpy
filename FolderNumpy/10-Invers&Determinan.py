import numpy as np

a = np.array([(1,-1),(1,1)])

print(a)

# inverse matrix
a_inv = np.linalg.inv(a)

print(a_inv)
print(np.dot(a,a_inv))

# determinan matrix

b_det = np.linalg.det(a)
b_det_inv = np.linalg.det(a_inv)
print(b_det)
print(b_det_inv)