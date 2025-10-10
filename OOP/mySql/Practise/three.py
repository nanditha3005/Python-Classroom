import mysql.connector
dbcon=None
dbcon=mysql.connector.connect(host="localhost",
                       user="root",
                       password="root",
                       database="dbone")
cursor=dbcon.cursor()
data=[(102,"sonia",23000.00),(103,"priyanka",20000.00),(104,"modi",30000.00)]
sql_st='''
        insert into employees(eid,ename,esal) values(%s,%s,%s)
      '''
cursor.executemany(sql_st,data)
print(cursor.rowcount)
dbcon.commit()

