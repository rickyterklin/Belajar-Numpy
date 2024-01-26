import numpy as np

# membuat vector
a = np.array([1,2,3,4,5])
b = np.array([1.5 , 2.5 , 3 , 4 , 5])

print(a)
print(b)

# membuat vector dengan range / interval
# seperti contoh di print dengan interval 2
c = np.arange(1,10,2)
print(c)

# membuat linespace
# menampilkan angka sesuai interval angka yg ditentukan 
# seperti contoh 4 maka menampilkan 4 angka dari 1-10 dengan jarak yg sama dst
d = np.linspace(1,10,4)
print(d)

# array multidimensi / matrix
e = np.array([(1,2,3),(4,5,6)])
print(e)
print(e+1)

# matrix dengan nilai nol
f = np.zeros((5,5))
print(f)

# matrix dengan nilai satu
g = np.ones((5,5))
print(g)

# matrix identitas
h1 = np.identity(7)
h2 = np.eye(3)

print(h1)
print(h2)


# display