import requests
import json

api_url = "https://api.exchangeratesapi.io/latest?base="

bozulan_doviz = input("Bozulan Döviz Türü: ")
alinanDoviz = input("Alınan Döviz Türü: ")
miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz? "))


result = requests.get(api_url+bozulan_doviz)

result = json.loads(result.text)

print(result)





