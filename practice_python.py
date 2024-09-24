import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = a * b
# print(c)

#--basics
a = np.array([1,2,3])
print(a)
#--2 dimension array
b = np.array([[1,2,3],[4,5,6]])
print(b)
# --get dimension
a.ndim
print(a.ndim)
print(b.ndim)
# get shape
a.shape
print(a.shape)
print(b.shape)
#  get type
a.dtype
print(a.dtype)
print(b.dtype)

print(a.dtype)
#  get the size
print(a.itemsize)
# compressing the data type
a = np.array([1,2,3], dtype = 'int32')
b = np.array([4,5,6])
print(a.dtype)
#  get the size
print(a.itemsize)
print(b.itemsize)
# get total size
print(a.nbytes)
