#same task but here need to use filter 
import pymongo
from pymongo import MongoClient
import requests 
#extract
url="https://dummyjson.com/products"
response_data=requests.get(url)
product_data=response_data.json()
products=product_data["products"]

#transform
beauty_products = list(filter(lambda product: product['category'] == 'beauty', products))
print(len(beauty_products))

#load
dbcon=pymongo.MongoClient('mongodb://localhost:27017/')
db=dbcon['dbone']
product_col=db['products']
product_col.insert_many(beauty_products)
print("data inserted successfully")


