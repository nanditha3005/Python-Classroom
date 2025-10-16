import pymongo
from pymongo import MongoClient
dbcon=MongoClient('mongodb://localhost:27017/')
db=dbcon['dbone']
user_col=db['users']

users=user_col.find()
for user in users:
    print(user['uname'])

user_col.update_one({"uid":103},{"$set":{'uname':'nanditha'}})

user_col.update_many({'uid':102},{'$set':{'sal':56000}})

user_col.delete_one({"uname":'rahul'})
user_col.delete_many({'uid':101})