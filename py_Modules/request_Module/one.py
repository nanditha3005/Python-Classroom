import requests
resp= requests.get('https://jsonplaceholder.typicode.com/user')
data=resp.json()
type(data)

import requests
resp=requests.get('https://dummyjson.com/products')
products=resp.json()
status_code=resp.status_code
print(products)

for product in products:
    print(products['products'])
