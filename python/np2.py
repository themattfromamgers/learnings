import numpy as np

result = np.array([10, 15, 30, 45, 60])

result = np.arange(5, 15)

result = np.arange(50,100, 5)

result = np.zeros(10)

result = np.ones(10)

result = np.linspace(0, 100, 5)

#Random Sayı
result = np.random.randint(10, 30, 5)

result = np.random.randn(10)

#Random 
result = np.random.randint(10, 50, 15).reshape(3, 5)

#RANDOM
matris = np.random.randint(10, 50, 15).reshape(3, 5)
print(matris)
# rowT = matris.sum(axis=1)
# colT = matris.sum(axis=0)
# print(matris)
# print(rowT)
# print(colT)


result = matris.max()
result = matris.min()
result = matris.mean()

result = matris.argmax()
result = matris.argmin()

arr = np.arange(10, 20)
# print(arr)
result = arr[::-1]

result = matris[0]

result = matris[1, 2]

result = matris**2

result = matris[matris %2 == 0]

print(result)