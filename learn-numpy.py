import numpy as np

# Creating a NumPy ndarray object

numpyArr = np.array([1, 2, 3, 4, 5])

print(numpyArr)
print(type(numpyArr))

# Checking the version of numpy
print(np.__version__)

# Use tuple to create a NumPy array
tupleArr = np.array((1, 2, 3, 4, 5))
print(tupleArr)

a = np.array(42) # 0D Array
b = np.array([1, 2, 3, 4, 5]) # 1D Array
c = np.array([[1, 2, 3, 7, 8], [4, 5, 6, 9, 10]])  #2D Array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])  #3D Array

print(a)
print(a.ndim)
print(b)
print(b.ndim)
print(c)
print(c.ndim)
print(d)
print(d.ndim)

# Higher Dimensional Arrays

hdArry = np.array([1, 2, 3, 4, 5], ndmin=5)
print(hdArry)
print('number of dimensions:', hdArry.ndim)

# Accessing Array elements

# 1D Array
print(b[3] + b[4])

# 2D Array
print(c[0, 1])
print(c[1, 4])

# 3D Array
print(d[0, 1, 2])

# Negative Indexing

print('Last element from 2nd dim: ', c[1, -1])

# NumPy Array Slicing

aSlice = np.array([1, 2, 3, 4, 5, 6, 7])
print(aSlice[1:5])