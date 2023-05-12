class nothesaplama:
    def __init__(self, ortalama1, ortalama2, performans):
        self.ortalama1 = ortalama1
        self.ortalama2= ortalama2
        self.performans = performans

class kullanici_girisi(nothesaplama):

    def __init__(self, ortalama1, ortalama2, performans):
        nothesaplama.__init__(self, ortalama1, ortalama2, performans)
        print("Kullanıcı Girişi Hazır")
    
    def ortalama1():
        global x
        x = int(input("Ortalama 1: "))

    def ortalama2():
        global y
        y = int(input("Ortalama 2: "))

    def performans():
        global z
        z = int(input("performans: "))
    
class sonuc(kullanici_girisi): 
    def __init__(self, ortalama1, ortalama2, performans):
        nothesaplama.__init__(self, ortalama1, ortalama2, performans)

    def girilenBilgiler():
        print(f'Not1:{x} \nNot2: {y}\nPerformans: {z}')

    def islem():
        global yeninot
        global eskinot
        eskinot = x+y+z
        yeninot = x+y+z/6
        
    def sonuc():
        print(f'Eski Not: {eskinot}\nYeni Not: {yeninot}')

class durum(sonuc):
     def __init__(self, ortalama1, ortalama2, performans):
        nothesaplama.__init__(self, ortalama1, ortalama2, performans)

     def GectiKaldi():
         
         if yeninot >= 100:
             print("Takdirle Geçtin")
         elif yeninot >= 50 and yeninot <100:
             print("Geçtin")
         else:
             print("kaldınız")

durum.ortalama1()




