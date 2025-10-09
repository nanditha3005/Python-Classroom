import mysql.connector
dbcon=None
dbcon=mysql.connector.connect(host="localhost",
                       user="root",
                       password="root",
                       database="onedb"
                        )
cursor=dbcon.cursor()
sql_st='''
         delete from employees where eid=103;
        '''
cursor.execute(sql_st)
dbcon.commit()