#Task 2:
#invoke rest api and print only beauty products 
#using for loop and while loop.
#API URL:https://dummyjson.com/products
#Method Method:GET
#Access Type:Public
#Required Fields:None

import requests
# Fetch API
resp = requests.get("https://dummyjson.com/products")
status_code = resp.status_code

if status_code == 200:
    data = resp.json()
    products = data["products"]   # list of products

    print(" Using for loop:")
    for product in products:
        if product["category"] == "beauty":
            print(product["title"])

    print("\n Using while loop:")
    i = 0
    while i < len(products):
        if products[i]["category"] == "beauty":
            print(products[i]["title"])
        i += 1
else:
    print("Failed to fetch data. Status code:", status_code)
