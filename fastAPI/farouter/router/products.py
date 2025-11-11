from fastapi import APIRouter

router=APIRouter(prefix="/products")
from pydantic import BaseModel


class products(BaseModel):
    pid:int
    pname:str
    price:float
    qty:int
    info:str
    
'''
Create product:
------------ 
Usage : Create new product 
URL : http://127.0.0.1:8000/product/create 
Method Type:POST 
Required Fields: pname,price,qty,info
Access Type:Public

'''
@router.post("/create")
def create_product():
    return {"msg":"New Product created"}


'''
Update Product:
------------ 
Usage : update product by Id
URL : http://127.0.0.1:8000/product/update/10
Method Type:PUT
Required Fields: pid,pname,qty,price  
Access Type:Public
'''
@router.put("/update/{pid}")
def update_product(pid:int):
    return {"msg":"Product updated successfully","pid":pid}


'''
Delete product:
------------ 
Usage : Delete product by Id
URL : http://127.0.0.1:8000/product/delete/101
Method Type:DELETE
Required Fields: None
Access Type:Public
'''
@router.delete("/delete/{pid}")
def delete_product(pid:int):
    return{"msg":"Product deleted","pid":pid}