
# class person:
#     pass

#     def __init__(self, name, year):
#      self.name = name
#      self.year = year
#      print("init methodu çalıştı")

#     def intro(self):
#      print("hello there")

#     def calculateaAge(self):
#         return 2019 - self.year
# p1 = person(name = 'B', year = 2000)
# p2 = person(name= 'C', year = 2002)

# p1.intro()


# #2
# class Circle:

#     pi = 3.14

#     def __init__(self, yaricap=1):
#         self.yaricap = yaricap
    
#     def cevre_hesapla(self):
#         return 2*self.pi+self.yaricap
#     def alan_hesapla(self):
#         return self.pi * (self.yaricap**2)

# c1 = Circle()
# c2 = Circle(5)

# print(f'c1: alan = {c1.alan_hesapla()} çevre: {c1.cevre_hesapla()}')

# print(f'c1: alan = {c2.alan_hesapla()} çevre: {c2.cevre_hesapla()}')


class kisiler():
    pass

    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        print("emthod çalıştı")
    
burak = kisiler(ad ='burak', soyad = 'yabgu', yas= 21)

cuce = kisiler(ad ='cansu', soyad = 'yabgu', yas= 211)

print(f'{burak.ad}, {burak.soyad}')
print(f'{cuce.ad}, {burak.soyad}')
   
    