from fastapi import FastAPI
from router.user import router as userrouter
from router.products import router as prodrouter

#create fast api app 
app=FastAPI()

#create root request
@app.get("/")
def index_page():
    return{"msg":"Application root request"}

app.include_router(userrouter)
app.include_router(prodrouter)


