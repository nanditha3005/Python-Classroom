#ask 1: invoke api and display all usernames
#API URL:https://jsonplaceholder.typicode.com/users
#Method Type:GET
#Access Type:public
#Required Fields: None

import requests
resp= requests.get('https://jsonplaceholder.typicode.com/users')
users=resp.json()
status_code=resp.status_code
print(users)
print(status_code)

#itterate using for 
for user in users:
 print("User Id:",user['id'],"-Name",user['username'])