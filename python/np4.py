import numpy as np

mylist = ["apple", "cherry", "banana"]
print(type(mylist))

myarray = np.array(mylist)
print(type(myarray))

print(myarray.ndim)


zero_Array = np.zeros((10,5))
print(zero_Array)
print("*")
transpose = zero_Array.T 
print(transpose)
print("**")

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

print(arr)
print(len(arr))
print("**")
reshape = np.reshape(arr, (4,3))
print(reshape)
print("**")

array1 = ([99, 33], [22, 15])
array2 = ([[55,47]])
concat = np.concatenate((array1, array2), axis=0)
print(concat)
print("*")

rangge = np.arange(1, 15.0)
print(rangge)

print("*")

# a = np.split(rangge,3)
b = np.array_split(rangge,3)
# print(a)
print(b)
print("**")
s = np.resize(reshape, (2,5))
print(s)
print("*")

print(reshape)
print("*")

del_reshape = np.delete(reshape, 0, 0)
print(del_reshape)
print("**")
print(np.__version__)
print("***")
arr = np.array([1, 2, 3, 4], ndmin=6)

print(arr)
print('number of dimensions :', arr.ndim)
print("**")
arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])
print("**")

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
print("**")
arrays = np.array([1, 2, 3 ])

tip = arrays.astype(str)
print(tip)
print(tip.dtype)
print("**")
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)
print("**") 


