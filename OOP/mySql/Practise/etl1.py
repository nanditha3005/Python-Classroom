import requests,mysql.connector,json,csv

response_data=requests.get('https://dummyjson.com/users')
print(response_data)                #<Response [200]>
print(type(response_data))         #<class 'requests.models.Response'>
print(response_data.status_code)    #200