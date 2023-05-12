import pandas as pd
import numpy as np
from numpy.random import randn

# numbers = np.array([20, 30, 40, 50])

# letters = ['a', 'b', 'c', 20]
# scalar = 5
# dict = {'a':10, 'b': 20, 'c': 30, 'd': 40}

# random_numbers = np.random.randint(100, 100, 6)

# pandas_seris = pd.Series(numbers)
# pandas_seris = pd.Series(scalar, [0, 1,2,3,4])
# pandas_seris = pd.Series(numbers, ['a', 'b', 'c', 'd'])
# pandas_series = pd.Series(random_numbers)

# pandas_series = pd.Series([20, 30, 40, 50], ['a', 'b', 'c', 'd'])

# resukt = pandas_series[['a', 'c', 'e']]
# resukt = pandas_series.ndim
# resukt = pandas_series.dtype
# resukt = pandas_series.shape
# resukt = pandas_series.sum()
# resukt = pandas_series.max()
# resukt = pandas_series.min()
# resukt = pandas_series + pandas_series
# resukt = np.sqrt(pandas_series)
# resukt = pandas_series >= 50
# resukt = pandas_series % 2 == 0 

# print(pandas_series)
# print(pandas_series[resukt])
# print(resukt)

# opel2018 = pd.Series([20, 30, 40, 10],["astra", "corsa", "mokka", "insig"])
# opel2019 = pd.Series([40, 30, 20, 10],["astra", "corsa", "GrandLand", "insig"])

# total = opel2018+opel2019
# print(total)

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# date = dict(apples = s1, oranges=s2)

# df = pd.DataFrame(date)
# print(df)

# data = [["ahmet", 50], ["mahmut", 25], ["burak", 11], ["tayyip", 50]]
# df = pd.DataFrame(data, [1,2,3,4],['Name', 'Puan'])

# dict = {"name": ["Ahmet", "Mehmet", "Ali", "Burcu"], "Puan": [20,30,40,31]}
# df = pd.DataFrame(dict, index=["212","232", "231", "162"])


# dict_list = [{"Name": "memet", "Grade": 50},
# {"Name": "mehmet", "Grade": 50},
# {"Name": "anan", "Grade": 62},
# {"Name": "mbaabt", "Grade": 31}]

# df = pd.DataFrame([1,2,3,4])
# print(df)
# df = pd.DataFrame(data, columns= ['Name', 'Puan'], index=[1,2,3,4])

# df = pd.DataFrame(dict)

# df = pd.DataFrame(dict_list)

# print(df)



# print("*")

#DOSYA OKUTMA

# df=pd.read_excel("Kitap.xlsx")
# print(df)

# print("*")


# df =pd.read_json("index.json")

# print(df)
# print("*")

# df = pd.DataFrame(randn(3,3), index = ['A', 'B', 'C'], columns=["Columun 1","Columun 2","Columun 3"])

# print(df)

# data = np.random.randint(10, 100, 75).reshape(15,5)
# df = pd.DataFrame(data, columns=["Col1","Col2","Col3","Col4","Col5"])

# d = data.min()
# dff = df.head(10)
# dff = df.tail(14) #tersten alma
# dff = df["Col1"].head()
# dff = df.columnsName.head()
# dff = df[["Col1", "Col2"]]
# dff = df[["Col1", "Col2"]].head()
# dff = df[["Col1", "Col2"]].tail()
# dff = df[5:15][["Col1", "Col2"]].head()
# dff = df[5:15][["Col1", "Col2"]].tail()
# dff = df > 50
# dff = df[df>50]
# dff = df[df & 2==0]
# dff = df[df["Col1"] > 50][["Col1", "Col2"]]
# dff = df[(df["Col1"] > 50) & (df["Col2"] <= 70)]
# dff = df[(df["Col1"] > 50) | (df["Col2"] > 50)][["Col1","Col2"]]

# dff = df.query("Col1 <= 50 & Col2 <= 50")

# print(df)
# print("Min: ", d)
# print(dff)

# personoller = {
    # 'Çalışanlar': ['Burak Yabgu', 'Uruz Tekin', 'Mirza', 'Umut Oreo'],
    # 'Meslek': ['Türkolog', 'Türkolog', 'Mafya', 'Pazarcı'],
    # 'Semt': ['GOP', 'BP', 'Esmezler', 'Bahçelievler'],
    # 'Maaş': [58000, 22000, 11500, 0],
    # 'Yaş': [22, 18, 18, 19]
    
# }

# b = pd.DataFrame(personoller)
# a = b["Maaş"]
# a = b.groupby("Maaş").groups
# a = b.groupby(["Meslek", "Semt"]).groups

# semtler= b.groupby("Semt")

# for name, group in semtler:
#     print(name)
#     print(group)
    
# for name, group in b.groupby("Maaş"):
#     print(name)
#     print(group)


# res = b.groupby("Semt").get_group("BP")
# res = b.groupby("Semt").sum()
# print(res)
print("*")
# res = b.groupby("Semt")["Maaş"].sum()
# res = b.groupby("Semt")["Maaş"].mean()
# res = b.groupby("Semt")["Çalışanlar"].count()
# res = b.groupby("Meslek")["Maaş"].max()
# res = b.groupby("Meslek")["Maaş"].max()["Mafya"]
# res = b.groupby("Meslek").agg(np.mean)
# res = b.groupby("Meslek")["Maaş"].agg([np.sum, np.mean,np.max, np.min])

# data = np.random.randint(10, 100, 15).reshape(5,3)


# df = pd.DataFrame(data, index = ['a', 'c', 'e', 'f','h'], columns=["col1", "col2", 'col3'])

# df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

# newCol = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 50]
# df["col4"] = newCol

# res = df.drop("col1", axis=1)
# res = df.drop(["col1", "col2"], axis=1)
# res = df.drop("a", axis=0)
# res = df.drop(["a", "b", "d"], axis=0)
# res = df.isnull()
# res = df.notnull()
# res = df.isnull().sum()
# res = df["col1"].isnull().sum()
# res = df[df["col1"].isnull()]
# res = df[df["col1"].isnull()]["col1"]
# res = df[df["col1"].notnull()]["col1"]

# res = df.dropna(axis = 1)
# res = df.dropna(how = "any")
# res = df.dropna(how = "all")

# res = df.dropna(subset = ["col1", "col2"])
# res = df.dropna(subset = ["col1", "col2"], how="any")
# res = df.dropna(subset = ["col1", "col2"], how="all")

# res = df.dropna(thresh = 2)
# res = df.dropna(thresh = 3)

# res = df.fillna(value = 'no input')
# res = df.fillna(value = 1)

# res = df.sum().sum()
# # res = df.size()
# res = df.isnull().sum()
# res = df.isnull().sum().sum()

print("***")

# data = pd.read_csv("nba.csv")

# data.dropna(inplace = True)

# data["Name"] = data["Name"].str.upper()
# data["Name"] = data["Name"].str.lower()
# data["index"] = data["Name"].str.find("a")
# data = data.Name.str.contains('Jordan')
# data = data[data.Name.str.contains('Jordan')]
# data = data.Team.str.replace(' ', '-').str.replace('')
# data[["FirstName", "LastName"]] = data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)
# print(data.head(10))


# customers = {
#     "CID": [1,2,3,4],
#     "FirstName": ["Ahmet", "Ali", "Mehmet", "Canan"],
#     "LastName": ["Ak", "Miyav", "Hamdi", "Çİftçioğlu"]
# }

# orders = {
#     "OrderID": [10,11,12,13],
#     "CID": [1,2,5,7],
#     "OrderDate": ['2010-7-10', '2013-7-10', '2012-7-10', '2015-7-10']
# }

# df_customers = pd.DataFrame(customers, columns=["CID", "FirstName", "LastName"])
# df_orders = pd.DataFrame(orders, columns=["OrderID", "Cid", "OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how="inner")

# print(result)


## ÇALIŞTI

# customers = {
#     'CustomerId': [1,2,3,4],
#     'FirstName': ["Ahmet","Ali","Hasan","Canan"],
#     'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# orders = {
#     'OrderId': [10,11,12,13],
#     'CustomerId': [1,2,5,7],
#     'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
# }

# df_customers = pd.DataFrame(customers, columns = ["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns = ["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how="inner")
# result = pd.merge(df_customers,df_orders,how="right")
# result = pd.merge(df_customers,df_orders,how="left")

customersA = {
    'CustomerId': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    'CustomerId': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Turan","Yılmaz","Turan"]
}

df_customersA = pd.DataFrame(customersA, columns = ["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns = ["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB])

print(result)