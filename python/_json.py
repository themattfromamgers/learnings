

#w dosya oluşturur
#a dosya üzerien yazar
#x dosya var mı yok mu kontrol eder
#r dosya okuması

#OTHER
# result = open("newfile.txt", "a", encoding='utf-8')
# print(result)
# result.write("\nheaa")
# result.close()

#OTHER
# try:
#     file = open("newfile.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("dosya bulanamıyor")
# finally:
#     print("dosya okumasu tamamlandı")
#     file.close()


#OTHER
# file = open("newfile.txt", "r", encoding="utf-8")

# content1 = file.read()
# print(content1)

#OTHER
# print(file.readline(), end="") 

#OTHER
# liste = file.readlines()
# print(liste)

#OTHER
# with open("newfile.txt", "r", encoding='utf-8') as file:
#     content = file.read()
#     print(content)

#OTHER
# with open("newfile.txt", "r+", encoding='utf-8') as file:
#     file.write("strss")

# with open("newfile.txt", "r+", encoding='utf-8') as file:
#     print(file.read())

with open("newfile.txt", "r+", encoding='utf-8') as file:
    list = file.readlines()
    list.insert(2, "\n Ali")
    print(list)
    file.seek(0)
    for i in list:
        file.write(i)
