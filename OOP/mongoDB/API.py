#invoke rest api and insert all beauty products into mongodb database
#API url=https://dummyjson.com/products
#method type=GET

import pymongo
from pymongo import MongoClient
import requests 
#extract
url="https://dummyjson.com/products"
response_data=requests.get(url)
product_data=response_data.json()
products=product_data["products"]

#transform
beauty_products=[]
# print(len(products))    #30
# print(type(products))   #<class'list'>

for product in products:
    if product['category']=='beauty':
        beauty_products.append(product)
print(len(beauty_products))     #5

#load
dbcon=pymongo.MongoClient('mongodb://localhost:27017/')
db=dbcon['dbone']
product_col=db['products']
product_col.insert_many(beauty_products)
print("data inserted successfully")


