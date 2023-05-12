def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 7 karakter olmalı")
    elif not re.search("[a-z]", psw):
        raise Exception("Parla küçük harfi çermeli")
    elif not re.search("[A-Z]", psw):
        raise Exception("Parla büyük harfi çermeli") 
    elif not re.search("[0-9]", psw):
        raise Exception("Parla rakam harfi çermeli")

    elif not re.search("[_@$]", psw):
        raise Exception("Parla alpharic harfi çermeli")  
    elif re.search("\s", psw):
        raise Exception("Parla küçük harfi çermeli")
    else:
        print("geçerli parola")
password = "1234567aaaA_"

try: 
    check_password(password)
except Exception as ex:
    print(ex)


