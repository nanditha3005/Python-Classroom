import requests,mysql.connector,json,csv 

resonse_data=requests.get('https://dummyjson.com/users')
print(resonse_data)               #<Response [200]>
print(type(resonse_data))          #<class 'requests.models.Response'>
print(resonse_data.status_code)    #200