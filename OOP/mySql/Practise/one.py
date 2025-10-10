import mysql.connector
dbcon=None
dbcon=mysql.connector.connect(host="localhost",
                              user="root",
                              password="root",
                              database="dbone"  
                              )
cursor=dbcon.cursor()
cursor.execute("create  table employees (eid int, ename varchar(25),esal float)")
dbcon.commit()
print('table created succesfully')

cursor.close()
dbcon.close()