import requests
from bs4 import BeautifulSoup

url = "https://metehan-altuntekin.github.io"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("main").find_all("section", {"id":"hero", "class": "side-gap"}, limit=10)

for i in list:
    title = i.find("h1").text
    print(title)
