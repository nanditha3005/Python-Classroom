import requests
import mysql.connector

url="https://dummyjson.com/users"
response=requests.get(url)

sql_users=[]
data=response.json()
users=data['users']

for user in users:
    sql_users.append((user['id'],user['lastName'],user['email'],user['gender']))


dbcon= mysql.connector.connect(host="localhost",
                               user="root",
                               password="root",
                               database="dbthree"
)
cursor=dbcon.cursor()

cursor.execute("DROP TABLE IF EXISTS sql_users")

sql_st1='''
CREATE TABLE IF NOT EXISTS sql_users(
user_id INT,
user_name VARCHAR(32),
email VARCHAR(50),
gender VARCHAR(6)
)
'''
cursor.execute(sql_st1)

#insert records
sql_st2='''
INSERT INTO sql_users(user_id, user_name, email, gender)
VALUES(%s,%s,%s,%s)
'''
cursor.executemany(sql_st2,sql_users)

#commit once
dbcon.commit()

#close connection
cursor.close()
dbcon.close()