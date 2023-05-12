class go():
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
        print("Went")

    def eat(self):
        print("i am eating")

class goes(go):
    def __init__(self, ad, soyad):
        go.__init__(self, ad, soyad)
        print("Student Created")
        
    def who_am_i(self):
        print("Hea")
s1 = go('Burak', 'Yabgu')
p1= goes('Umut', 'Oreo')

print(s1.ad + ' ' + s1.soyad)





