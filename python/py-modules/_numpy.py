import pandas as pd
import numpy as np

# NUMPY KOMUTLARI


# NUMPY
a = np.linspace(1, 100, 10)
print(a)
a = np.arange(1, 100)
print(a)

a = np.zeros(5)
print(a)
a = np.ones(5)
print(a)

veri = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
npVeri = veri.reshape(3, 3)
print(npVeri)

print(npVeri.shape)

print(npVeri.ndim)

print("*")

numbers = np.random.randint(10, 100, 6)

print(numbers)

re = np.sin(numbers)
re2 = np.cos(numbers)
re3 = np.sqrt(numbers)
re4 = np.log(numbers)
print(re)
print(re2)
print(re3)
print(re4)

#BİRLEŞTİRME
print("*")

numbers = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

numbers1n = numbers.reshape(2, 3)
numbers2n = numbers2.reshape(2, 3)

result = np.vstack((numbers1n, numbers2n))
print(result)

print("*")

a = result.min()
print("En küçük sayı: ", a)

a = result.max()
print("En büyük sayı: ", a)

a = result.mean()
print("Ortalama sayı: ", a)

a = result.argmax()
b = result.argmin()
print("argmax: ", a)
print("argmin: ", b)
#
arr = np.arange(0, 10)
arr2 = arr.copy()
print(arr)
print(arr2)
#
print("*")
list1 = ([33, 10], [20, 00])
list2 = ([[31, 21]])
listTopla = np.concatenate((list1, list2), axis=0)
print(listTopla)

print("*")

rangge = np.arange(1, 15.0)
print(rangge)

print("*")

b = np.array_split(rangge,3)
print(b)

print("*")

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
reshape = np.reshape(arr, (4,3))

s = np.resize(reshape, (2,5))
print(s)

print("*")
del_reshape = np.delete(reshape, 0, 0)
print("Silindi:", del_reshape)

print("*")

arr = np.array([1, 2, 3, 4], ndmin=6)

print(arr)

print("*")

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

print("*")

arrays = np.array([1, 2, 3 ])
tip = arrays.astype(str)
print(tip)
print(tip.dtype)
print("**")
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)
print("**") 

a = np.matrix([[1,2], [3,4]])
print(a[1])


