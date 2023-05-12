# -*- coding: utf-8 -*-

# -- Main --

# ENUMERATE
x = ('elma', 'muz', 'kavun') 
y = "karpuz"

print(list(enumerate(x, start=3)))
print(list(enumerate(y)))

print(type(x))
print(type(y))

# enumerate - 2 kullanım
meyveList = ['elma', 'karpuz', 'kavun', 'çilek']

for sira, meyve in enumerate(meyveList, start=1):
    print(f'{sira}. Meyve: {meyve}')

meyveList = ['elma', 'karpuz', 'kavun', 'çilek']
sıraList = [1,2,3,4]

for dongu in zip(meyveList, sıraList):
    print(dongu)

# ZIP

a = ("Burak", "Umut", "Mirza", "Belirsiz")
b = ("Yabgu", "Oreo", "ÇakmaMafyaoğlu")

x = zip(a, b)
print(list(x))

#REDUCE


# Using a pre-defined function
from functools import reduce

def sumTwo(a,b):
    return a+b

result = reduce(sumTwo, [1, 2, 3, 4])
print(result)


numbers = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, numbers) # returns 10
print(suma)


#


from functools import reduce
numbers = [1, 2, 3, 4]
def sum(a, b):
    return a + b
# Call sum() function on each element accumulatively
total = reduce(sum, numbers)
print(total)

from functools import reduce

def toplama(x, y):
    return x + y
def carpma(x, y):
    return x*y

liste =  [3,3,3]

sonuc1 = reduce(toplama, liste)
sonuc2 = reduce(carpma, liste)
print(sonuc1)
print(sonuc2)

# MAP

def addition(n):
    return n + n
  
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# MAP 2

numbers = [2, 4, 6, 8, 10]

def square(number):
  return number * number

squared_numbers_iterator = map(square, numbers)

squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# MAP 3 -D

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# MAP

liste1 = [5, 4, 3, 6]
liste2 = [5, 4, 3, 6] 

def toplam(x, y):
    return x+y
sonuc = list(map(toplam, liste1, liste2))

print(sonuc)

