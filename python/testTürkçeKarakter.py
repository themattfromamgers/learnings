
def go(ad):

    yasakli_adlar = "1234567890"

    for i in ad:
        if i in yasakli_adlar:
            raise TypeError("yasakli ad")
        else:
            print("sorun yok")
    print("başarılı")

ad = input("ad: ")

try:
    go(ad)
except TypeError as e:
    print("hata:\n", e)

