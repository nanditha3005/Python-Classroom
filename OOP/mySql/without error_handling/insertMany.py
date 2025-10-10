import mysql.connector
dbcon=None
dbcon=mysql.connector.connect(host="localhost",
                       user="root",
                       password="root",
                       database="onedb"
                        )
cursor=dbcon.cursor()
data=[(102,"sonia",3500.00),(103,"priyanka",24000.00),(104,"nand",25600.00)]
sql_st='''
          insert into employees(eid,ename,esal) values(%s,%s,%s)
        '''
cursor.executemany(sql_st,data)
print(cursor.rowcount)

dbcon.commit()
cursor.close()
dbcon.close()