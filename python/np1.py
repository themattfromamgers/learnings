from random import randint
import numpy as np
print("*****************")
py_list = [1,2,3,4,5,6,7,8,9]

np_arrays = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(type(py_list))
print(type(np_arrays))

py_multi = [[1,2,3], [4,5,6], [7,8,9]]
np_multi = np_arrays.reshape(3, 3)
print(py_list)
print(np_multi)

print(np_arrays.ndim)
print(np_multi.ndim)

print(np_arrays.shape)
print(np_multi.shape)

#2

result = np.array([1,3,5,7,9])
print(result)
result2 = np.arange(1, 10)
print(result2)
result3 = np.arange(10, 100, 3)
print(result3)
result4 = np.zeros(10)
print(result4)
result5 = np.ones(10)
result6 = np.linspace(0, 100, 5)
result7 = np.linspace(0, 5 , 5)

result8 = np.random.randint(0, 10)
result9 = np.random.randint(20)

result10 = np.random.randint(1, 10, 3)
result11 = np.random.rand(5)
result12 = np.random.randn(5)
result13 = np.arange(50)

np_array = np.arange(50)
np_multi = np_array.reshape(5, 10)

print(np_multi.sum(axis=0))
print(np_multi.sum(axis=1))


rnd_numbers = np.random.randint(1, 100, 10)
print(rnd_numbers)

resultMAX = rnd_numbers.min()
print("MAX: ", resultMAX)
resultMIN = rnd_numbers.max()
print("MIN: ", resultMIN)
result = rnd_numbers.mean()
print("mean: ", result)

argx = rnd_numbers.argmax()
print(argx)
arg = rnd_numbers.argmin()
print(arg)

numbers = np.array([5, 10, 15, 20, 25, 50, 75])

result = numbers[6]

print(result)
print(numbers[-2])
print(numbers[0:3])
print(numbers[0:3])
print(numbers[:3])
print(numbers[3:])
print(numbers[::])
print(numbers[::-1])

print(numbers[::-2])
print("****************")
numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]])

print(numbers2[1])
print(numbers2[0, 2])
print(numbers2[2, 1])
print(numbers2[:,2])
print(numbers2[:,0])
print(numbers2[:,0:2])
print(numbers2[-1, :])
print("3 SÜTUN", numbers2[:3, :3])
print(numbers2[:2, :2])
print("****************")

arr = np.arange(0, 10)
arr2 = arr.copy()
print(arr)
print(arr2)

arr2[0] = 20
print(arr)
print(arr2)
print("****************")

numbers = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print(numbers)
print(numbers2)
print("*")
result = numbers+numbers2
result2 = numbers+ 10
tt = numbers-numbers2 

print(result)
print(result2)

print(tt)

print("********************")

numbers = np.random.randint(10, 100, 6)
numbers2 = np.random.randint(10, 100, 6)

print(numbers)
print(numbers2)

re = np.sin(numbers)
re2 = np.cos(numbers)
re3 = np.sqrt(numbers)
re4 = np.log(numbers)
print(re)
print(re2)
print(re3)
print(re4)

numbers1n = numbers.reshape(2, 3)
numbers2n = numbers2.reshape(2, 3)

result = np.vstack((numbers1n, numbers2n))

print(numbers1n)
print(numbers2n)
print("*")
print(result)

print(numbers)
re = numbers >= 50
print(re)
print(re[1])
