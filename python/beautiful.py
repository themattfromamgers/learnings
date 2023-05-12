from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buvak</title>
</head>

<body>
    <div class="grup1">
        <h2>Programlama</h2>
        <ul>
            <li>Menü 1</li>
            <li>mENÜ 2</li>
            <li>Menü 3</li>

        </ul>
    </div>


    <div class="grup2">
        <h2>Modüller</h2>
        <ul>
            <li>Menü 1</li>
            <li>mENÜ 2</li>
            <li>Menü 3</li>
            <a class="sister" href="https://www.youtube.com" id="link1">Linkimiz</a>

        </ul>
    </div>

</body>

</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

result =  soup.prettify()
result1 = soup.title #direk etiket ve içindekini
result = soup.title.name # Etiket adını
result = soup.title.string # Etiket içindeki değeri alıyor

result22 = soup.find_all("h2")[0]
result2 = soup.find_all("h2")
print(result22)
print(result2)
print("***********************")
print(result)
print(result1)
print("**********************************")

resu = soup.find_all("div")
print(resu)
print("*********************************")
res = soup.find_all("div")[1].ul
re = soup.find_all("div")[1].ul.find_all("li")
print(res)
print("**************")
print(".find_all li:  ", re)
print("**************")
ress = soup.div.findChildren() 
print(ress)

print("------------------")
result = soup.div.findNextSibling().findNextSibling()
print(result)
print("------------------")
resu = soup.find_all('a')

print(resu)
