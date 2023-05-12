
from yabguu import *

try:
    x = int(input("y:"))
    y = int(input("z: "))
    print(x/y)
except ZeroDivisionError:
    print("0 ile bölünemez kardeş") 
except ValueError as e:
    print("Sadece sayı girebilirsiniz.\nHata Türü:", e)
else:
    print("herşey yolunda")
finally:
    print("komuttan çıkıldı")


print("xd")















