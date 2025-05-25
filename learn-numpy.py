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

# Array Slicing Steps

print(aSlice[1:5:2])
print(aSlice[::2])

bSlice = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(bSlice[1, 1:4])
print(bSlice[0:2, 2])
print(bSlice[0:2, 1:4])

# Data Types in NumPy

# Checking the data type of an array

dataType = np.array([1, 3, 5, 7, 9])
print(dataType.dtype)

dataType2 = np.array(['apple', 'banana', 'cherry'])
print(dataType2.dtype)

# Creating arrays with defined data type

dataType3 = np.array([1,2,3,4,5], dtype='S')
print(dataType3)
print(dataType3.dtype)

# dataType4 = np.array(['a', '2', '3'], dtype='i')
# print(dataType4)
# print(dataType4.dtype)

# Converting data type on existing arrays
dataType5 = np.array([1.1, 2.1, 3.1])

newarr = dataType5.astype('i')
print(newarr)
print(newarr.dtype)

# or using 'int' as parameter value

newarr2 = dataType5.astype(int)

print(newarr2)
print(newarr2.dtype)

# Change data types from integer to boolean

dataType6 = np.array([1, 0, 3])

newarr3 = dataType6.astype(bool)

print(newarr3)
print(newarr3.dtype)

# NumPy Array copy vs view

# Copy

aCopy = np.array([1, 2, 3, 4, 5, 6])
x = aCopy.copy()
aCopy[0] = 42

print(aCopy)
print(x)

# View

bCopy = np.array([1, 2, 3, 4, 5, 6, 7])
y = bCopy.view()
bCopy[0] = 42

print(bCopy)
print(y)

# Make changes in the view

y[0] = 31

print(bCopy)
print(y)

# Check if array owns its data
print(x.base)
print(y.base)

# NumPy Array shape

arrShape = np.array([[1, 2, 3, 7, 8], [4, 5, 6, 9, 10]])

print(arrShape.shape)

arrShape2 = np.array([1, 2, 3, 4], ndmin=5)

print(arrShape2)
print('Shape of array :', arrShape2.shape)

# NumPy Joining Arrays

arrJoin = np.array([1, 2, 3])
arrJoin2 = np.array([4, 5, 6])

arrJoin3 = np.concatenate((arrJoin, arrJoin2))
print(arrJoin3)

# Join 2D array along rows (axis=1)

arrJoin4 = np.array([[1, 2], [3, 4]])

arrJoin5 = np.array([[5, 6], [7, 8]])

arrJoin6 = np.concatenate((arrJoin4, arrJoin5), axis=1)
print(arrJoin6)

# Joining Arrays using the stack functions

arrJoin7 = np.stack((arrJoin, arrJoin2), axis=1)
print(arrJoin7)

# Stacking along rows

arrJoin8 = np.hstack((arrJoin, arrJoin2))
print(arrJoin8)

# Stacking along columns

arrJoin9 = np.vstack((arrJoin, arrJoin2))
print(arrJoin9)

# Stacking along height (depth)

arrJoin10 = np.dstack((arrJoin, arrJoin2))
print(arrJoin10)

# NumPy splitting array

arrSplit = np.array([1, 2, 3, 4, 5, 6])

arrSplit1 = np.array_split(arrSplit, 3)
print(arrSplit1)
print(arrSplit1[0])
print(arrSplit1[1])
print(arrSplit1[2])

arrSplit2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

arrSplit3 = np.array_split(arrSplit2, 3)
print(arrSplit3)

arrSplit4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

arrSp = np.hsplit(arrSplit4, 3)

print(arrSp)


# NumPy Searching Arrays

arrSearch = np.array([1, 2, 3, 4, 5, 4, 4])

xSearch = np.where(arrSearch == 4)
print(xSearch)

ySearch = np.where(arrSearch % 2 == 0)
print(ySearch)

ySearch = np.where(arrSearch % 2 == 1)
print(ySearch)

# NumPy Sorting Arrays

arrSort = np.array([3, 2, 0, 1])
print(np.sort(arrSort))

arrSort2 = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arrSort2))

arrSort3 = np.array([True, False, True])
print(np.sort(arrSort3))

# Sorting a 2D array

arrSort4 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arrSort4))

# NumPy Filter Array

arrFilter = np.array([41, 42, 43, 44])
xFilter = [True, False, True, False]

newarrFilter = arrFilter[xFilter]
print(newarrFilter)

filter_arr = []

for element in arrFilter:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
    
newarrFilter2 = arrFilter[filter_arr]
print(filter_arr)
print(newarrFilter2)

# Creating Filter Directly from Array

filter_arr2 = arrFilter > 42

newarrFilter3 = arrFilter[filter_arr2]

print(filter_arr2)
print(newarrFilter3)

# Random Numbers in NumPy

# Generate random number

from numpy import random

xRandom = random.randint(100)
print(xRandom)

# Generate random float

yRandom = random.rand()
print(yRandom)

# Generate random array

zRandom = random.randint(100, size=5)
print(zRandom)

aRandom = random.randint(100, size=(3, 5))
print(aRandom)


bRandom = random.rand(5)
print(bRandom)

cRandom = random.rand(3, 5)
print(cRandom)

# Generate random number from array

dRandom = random.choice([3, 5, 7, 9])
print(dRandom)

eRandom = random.choice([3, 5, 7, 9], size=(3, 5))
print(eRandom)


# Seaborn

# Plotting a displot
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0, 1, 2, 3, 4, 5])

plt.show()

# Plotting a displot without the histogram

sns.displot([0, 1, 2, 3, 4, 5, 6], kind='kde')

# Visualization of Normal distribution

sns.displot(random.normal(size=1000), kind="kde")

plt.show()