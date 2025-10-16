#path parameter is a part of url wch is used to identify specific resource
#http://127.0.0.1.8000/users
#http://127.0.0.1.8000/users/addusers
#http://127.0.0.1.8000/users


from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
users=[]
'''
usage:Application Root Request
API URL:http://127.0.0.1:8000/ 
Method :GET
Required Fields:None
'''
@app.get("/")
def home_page():
    return{"message":"Application Home Page"}


'''
usage:Dispalyig all users
API URL:http://127.0.0.1:8000/users
Method:GET
Required Fields:None
'''
@app.get("/users")
def fetch_users():
    return{"message":"Displaying users"}


'''
usage:Fetch all users
API URL:http://127.0.0.1:8000/users/
Method:GET
Required Fields:None
'''

@app.get("/users/{uid}")
def get_users():
    return users


class User(BaseModel):
    uid:int
    uname:str
    loc:str



'''
usage:Create new user
API URL:http://127.0.0.1:8000/users/
Method:POST
Required Fields:uid,uname,loc
'''
@app.post("/users")
def create_user(user:User):
    print(user)
    users.append(user)
    return{"message":"new user created","user":user}


