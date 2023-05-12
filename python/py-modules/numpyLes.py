# -- One_Numpy --

import numpy as np
mylist = ["apple", "cherry", "banana"]
print(type(mylist))

myarray = np.array(["apple", "cherry", "banana"])
print(type(myarray))

second_arrays = np.array([1,2,3,4,5,6,7,8,9])
print(type(second_arrays))
print(second_arrays)

two_aray = second_arrays.reshape(3, 3)
print(two_aray)

print("Byte: ", second_arrays.ndim)
print("Byte: ", two_aray.ndim)

print(second_arrays.shape)
print(two_aray.shape)

arrays = np.array([1, 2,3,4,5,6,7,8,9])
three_vers_arrays = arrays.reshape(3, 3)

print(three_vers_arrays)

# -- Two_Numpy --

import numpy as np
arrays = np.array([1, 2,3,4,5,6,7,8,9, 10, 11, 12])
three_vers_arrays = arrays.reshape(4, 3)

print(three_vers_arrays)
print(three_vers_arrays.ndim)

result = np.array([1, 3, 5, 7, 9])
print(result)

result = np.arange(1, 10)
print(result)

result = np.arange(10, 100, 3)
print(result)

zerosarray = np.zeros((5, 3))
print(zerosarray)

import numpy as np
print(np.__version__)

# -- w3_Numpy --

arr = np.array((1, 2, 3, 4, 5))

print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=6)

print(arr)
print('number of dimensions :', arr.ndim)

#TOPLAMA
arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

print('5th element on 2nd row: ', arr[1, 4])

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)


arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)

arrays = np.array([1, 2, 3 ])

tip = arrays.astype(str)
print(tip)
print(tip.dtype)

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)



