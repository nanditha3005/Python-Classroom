from fastapi import APIRouter

router=APIRouter(prefix="/user")

from pydantic import BaseModel

class user(BaseModel):
    uid:int
    uname:str
    email:str
    gender:str
    loc:str


'''
Create User:
------------ 
Usage : Create new User 
URL : http://127.0.0.1:8000/user/create 
Method Type:POST 
Required Fields:uid,uname,email,gender,loc
Access Type:Public
'''
@router.get('/create')
def create_user():
    return{"msg":"New user created"}



'''
Read Users:
------------ 
Usage : Fetch all users 
URL : http://127.0.0.1:8000/user/ 
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@router.get("/")
def fetch_all_users():
    return {"msg":"Fetching all users"}



'''
Read User:
------------ 
Usage : Fetch user by Id
URL : http://127.0.0.1:8000/user/101
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@router.get("/{uid}")
def get_user(uid:int):
    return {"msg":"Fetching user details",'uid':uid}



'''
Update User:
------------ 
Usage : update user by Id
URL : http://127.0.0.1:8000/user/update/101
Method Type:PUT
Required Fields:uid,uname,email,gender,loc  
Access Type:Public
'''
@router.put("/update/uid")
def update_user(uid:int):
    return{"msg":"User updated successfully","uid":uid}



'''
Delete User:
------------ 
Usage : update user by Id
URL : http://127.0.0.1:8000/user/delete/101
Method Type:DELETE
Required Fields:uid,uname,email,gender,loc  
Access Type:Public

'''
@router.delete('/delete/{uid}')
def delete_user(uid:int):
    return{"msg":"user deleted successfully","uid":uid}



