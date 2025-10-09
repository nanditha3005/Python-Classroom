import mysql.connector
dbcon=mysql.connector.connect(host="localhost",
                       user="root",
                       password="root",
                       database="onedb"
                        )
cursor=dbcon.cursor()
cursor.execute("select * from employees")
# dbcon.commit()
data=cursor.fetchall()
print(data)

for user in data:
    print(user)





                             