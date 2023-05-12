# class Person:
#     pass

#     address = "No İnfermation"

#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
    
#     def intro(self):
#         print('Hello There '+self.name)
        
#     #instance methods
#     def calculateAge(self):
#         return 2022 - self.year
    
    
#objects instance
# p1 = Person('ali', 2000)
# p2 = Person('yagmur', 2002)

# p1.intro()
# p2.intro()


# print(f' adım {p1.name} ve yaşım {p1.calculateAge()}')
# print(f' adım {p2.name} ve yaşım {p2.calculateAge()}')

# UPDATE
# p1.name = "Amed"
# p1.address = "ANGARA"


# print(f'name: {p1.name} year: {p1.year} address: {p1.address}')
# print(f'name: {p2.name} year: {p2.year} address: {p2.address}')

# print(p1)
# print(p2)
# print(type(p2))
# print(p1 == p2)


# 2

# class Circle:
    # Class object attribute (coa)
    # pi = 3.14
    
    # def __init__(self, yaricap=1):
        # self.yaricap = yaricap
        
    # Methods
    
    # def cevre_hesapla(self):
        # return 2 * self.pi * self.yaricap
    
    # def alan_hesapla(self):
        # return self.pi * (self.yaricap**2)


# c1 = Circle() # yari cap = 1
# c2 = Circle(5)

# print(f'c1: alan = {c1.alan_hesapla()} çevre: {c1.cevre_hesapla()}')    
# print(f'c2: alan = {c2.alan_hesapla()} çevre: {c2.cevre_hesapla()}')    


# 3

# Inheritance

# class Person():
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         print("Person Created")
        
#     def whi_am_i(self):
#         print("I am a person")
        
#     def eat(self):
#         print("Eating..")
    
# class Student(Person):
#     def __init__(self, fname, lname, number):
#         Person.__init__(self, fname, lname)
#         self.number = number
#         print('Student Created')
    
#     #ovveride
#     def who_am_i():
#         print('I AME M')
        
#     def sayHello(self):
#         print("Miraba")

# class Teacher(Person):
#     def __init__(self, fname, lname, branch):
#         super().__init__(fname, lname)
#         self.branch = branch
#     def whi_am_i(self):
#         print(f'I am a {self.branch} teacher')
    

# p1 = Person('Ali', 'Yılmaz')
# s1 = Student("Çınar", "Turan", 1256)
# t1 = Teacher('Buvak', 'Yabgu', 'Matematik')

# print(p1.fname + ' ' + p1.lname)
# print(s1.fname + ' ' + s1.lname + ' ' + str(s1.number))

# p1.whi_am_i()
# s1.whi_am_i()
# t1.whi_am_i()

# p1.eat()
# s1.eat()

# s1.sayHello()




#     SPECIAL METHODS

# mylist = [1,2,3]
# mystring = 'my string'
# print(len(mylist))
# print(type(mylist))
# print(len(mystring))
# print(type(mystring))

class Movie():
    
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu')
    def __str__(self):
        return f'{self.title} by {self.director}'
    
    def __len__(self):
        return self.duration
    def __del__(self):
        print("obje silindi")

m = Movie('film adı', 'yönetmen adı', 120 )


del m

print(m)


