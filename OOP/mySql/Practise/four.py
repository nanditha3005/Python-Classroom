import mysql.connector
dbcon=None
dbcon=mysql.connector.connect(host="localhost",
                              user="root",
                              password="root",
                              database="dbone")
cursor=dbcon.cursor()
sql_st='''
        update employees set esal=null where eid=103;
       '''
cursor.execute(sql_st)
dbcon.commit()