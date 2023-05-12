import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://burakyabgu:123@cluster0.ujtc9.mongodb.net/?retryWrites=true&w=majority")


db = myclient["me"]
col = db["test"]

# VERİ GÖNDERDİK
# veri = {
#     "_id": 1,
#     "adi": "burak",
#     "soyadi": "yabgu",
#     "yasi": 18
# }
# x = col.insert_one(veri)


# TOPLU GÖNDERME
# telefon_list = [
#     {"name":"Samsung S6", 
#     "fiyat": 3000, 
#     "aciklama":"iyi telefon"},
    
#     {"name":"Samsung S7", 
#     "fiyat": 4000, 
#     "kategori": ['telefon','elektronik']}
# ]

# result = col.insert_many(telefon_list)
# print(result.inserted_ids)

# ------>> VERİ İÇERİSİNDEKİ DEĞERİ ÇEKER
# for i in col.find():
#     pass

# x = i.get("parola")
# print(x)

# ------>> 

#SORGU

# filter = {"name": "Samsung S7"}
# res = col.find(filter)
# for i in res:
#     print(i)


# res = col.find_one({"_id": ObjectId("628ecc40207b894b18f01aee")})
# print(res)

# BELİRLİ ARAMA
# result = col.find({
#     "name": {
#         "$in": ["Samsung S5", "Samsung S6", "Samsung S7"]
#     }
# }) 

# büyük $gt
# result = col.find({
#     "fiyat": {
#         "$gt": 2000
#     }
# })

# BÜYÜK EŞİT $gte
# result = col.find({
#     "fiyat": {
#         "$gte": 2000
#     }
# })

# eşit olan kayıtlar gelir
# result = col.find({
#     "fiyat": {
#         "$eq": 4000
#     }
# })


# result = col.find({
#     "fiyat": {
#         "$lte": 4000
#     }
# })

# İSTEDİĞİNİZ ŞEYİ, BİR DEĞERDE ARATIR
# result = col.find({
#     "name": {"$regex": "^Ğ"}
# })

# for i in result:
#     print(i)

# ------>

# result = col.find().sort("name", 1)
# result = col.find().sort("name", -1)

# for i in result:
#     print(i)

# ------>

# for i in col.find():
#     print(i)

# TEK VERİ UPDATE
# col.update_one(
#     {'name': "Samsung S6"},
#     {'$set':{
#         "name": "Iphone X Plus",
#     }}
# )

# ÇOKLU VERİ UPDATE
# col.update_many(
#     {'name': "Iphone Gold Plus"},
#     {'$set':{
#         "name": "Iphone Ultimate Gold Plus",
#         "fiyat": 10000000
#     }}
# )

# aynı mantık ama bölünmüş 
# oldVal = {'name': 'Iphone Ultimate Gold Plus'}
# newVal = {
#     "$set": {
#         "name": "Léonlight s5",
#         "fiyat": 100
#     }
# }

# col.update_many(oldVal,newVal)


# print("*")
# for i in col.find():
#     print(i)

# TEK SİLME İŞLEMİS
# col.delete_one({
#     "name":"Samsung S7"
# })

# ÇOKLU SİLME
col.delete_many({
    "name":{"$regex": "^Huawei"}
})

print("*")
for i in col.find():
    print(i)