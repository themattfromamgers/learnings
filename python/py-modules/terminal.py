import os
from datetime import datetime
import pandas as pd
def runpy():
    fileName = input("dosya adı: ")
    runPyTest = lambda: os.system(f"py -m pytest {fileName}")
    runPyTest()
    return " "

def runpyFileSpace():
    runPyTest = lambda: os.system(f"py -m pytest .")
    runPyTest()
    return " "

def pyRun():
    fileName = input("dosya adı: ")
    runPY = lambda: os.system(f"python {fileName}")
    runPY()
    return " "

def test():
    
    simdi = datetime.now()
    tarih = f"{simdi.day}, {simdi.month},{simdi.year}"
    saat = f"{simdi.hour},{simdi.minute},{simdi.second}"
    liste = [["He", "Ha", tarih,saat]]
    
    Read_now = pd.DataFrame(liste, columns=["Güncelleme", "Dosya Adı", "Tarih", "Saat"])
    
    print(Read_now)
    
    return " "

def default():
    return "Yanlış"

komutlar = {
    "tes": test,
    "pt": runpy,
    "p": pyRun,
    "pt .": runpyFileSpace
    }
def switch(case):
    return komutlar.get(case, default)()
while True:
    title = lambda: os.system("title Worksplace by Burak Yabgu")
    title()
    komut = input("~# ")
    print(switch(komut))