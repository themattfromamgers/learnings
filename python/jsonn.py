import json





kisi_dict = {
    'isim': 'Deniz',
    'yas': 12,
    'cinsiyet': 'K'
}

with open('kisi.json', 'w') as json_dosya:
    json.dump(kisi_dict, json_dosya)
print("******************")
with open('kisi.json') as f:
    veri = json.load(f)

print(veri)