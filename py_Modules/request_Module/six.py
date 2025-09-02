#Task 2:
#invoke rest api and print only beauty products 
#using for loop and while loop.
#API URL:https://dummyjson.com/products
#Method Method:GET
#Access Type:Public
#Required Fields:None

     #using sir concept

import requests
resp=requests.get('https://dummyjson.com/products')
product_data=resp.json()
products=product_data['product']
no_of_beauty_products=0

for product in products:
    if product['category']=='beauty':
        print(product['title'])
        no_of_beauty_products=no_of_beauty_products+1

print('no_of_beauty_products')


