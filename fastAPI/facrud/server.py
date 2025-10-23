from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
users=[]

class User(BaseModel):
    name:str
    email:str
    mobile:int 


'''
usage:Application Root Request
API URL:http://127.0.0.1:8000/
Method :GET
Required fields:None
'''
@app.get('/')
def home_page():
    return {"msg":"Application Root"}


'''
Usage:Create new user
API URL:http://127.0.0.1:80000/create
Method Type:POST
Required Fields:Uname,email,mobile
Access Type:Public
'''
@app.post('/create')
def create_user(user:User):
    users.append(user)
    return {"msg":"new user created" ,"user":user}


'''
Usage:fetch user
API URL:http://127.0.0.1:80000/read
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get('/read')
def get_user():
    return{"msg":"fetch all users"}



'''
Usage:Update  user
API URL:http://127.0.0.1:80000/update
Method Type:PUT
Required Fields:Uname,email,mobile
Access Type:Public
'''
@app.put('/update/{uid}')
def update_user(uid:int):
    print(uid)
    return{"msg":"user updated","uid":uid}


'''
Usage:Delete user by uid
API URL:http://127.0.0.1:8000/delete/101
Method Type:DELETE
Required Fields:Uname,email,mobile
Access Type:Public
'''
@app.delete('/delete/{uid}')
def delete_user(uid:int):
    print(uid)
    return{"msg":"user deleted","uid":uid}