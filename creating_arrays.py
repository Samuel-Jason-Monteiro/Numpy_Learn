import numpy as np 

# by passing list
arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


# by passing tuple
arr2 = np.array((1, 2, 3, 4, 5))

print(arr2)

print(type(arr2))


# 0D array
a = np.array(45)
print(a)

# 1D array
b = np.array([1, 4, 6])
print(b)

# 2D array
c = np.array([[1,2,3,4], [5,6,7,8]])
print(c)

# 3D array
d = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print(d)

#  checking dimension
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

n = np.array([1,2,3,4], ndmin = 5)
print(n)
