#  invoke Rest API
#  https://jsonplaceholder.typicode.com/users
#  and 1.write users data into user.json file 
# and 2.write into user.csv  
# user.csv
# uid,uname,city,phoneno


import requests,json
response=requests.get('https://jsonplaceholder.typicode.com/users')
users=response.json()
#print(users)
print(type(users))

new_users=[]

for user in users:
    new_users.append({ 'id':user['id'],'name':user['username'], 'city':user['address']['city']})

print(new_users)


fp1=open('users.json','w')

json.dump(new_users,fp1)
print('New JSON File Created')
