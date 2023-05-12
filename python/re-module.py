import re
satir = "İleri Seviye Java: Java ile programlama kursu"

# result = re.findall("Java", satir)
# result = len(result)

# result = re.split(" ", satir)
# result = re.split("R", satir)


# result = re.sub(" ", "-", satir)
# result = re.sub("\s", "-", satir)

result = re.search("Java", satir)



print(result)