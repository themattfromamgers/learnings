


def checkPassword(parola):

    turkce_karakterler = "çşiğüö"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola Türkçe Karakter i içeriyor")
        else:
            pass
    print("geçerli parola")

    parola = input("parola :")

try:
    checkPassword(parola)
except TypeError as err:
    print(err)