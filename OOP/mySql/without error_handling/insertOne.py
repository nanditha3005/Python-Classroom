import mysql.connector
dbcon=None
dbcon=mysql.connector.connect(host="localhost",
                       user="root",
                       password="root",
                       database="onedb"
                        )
cursor=dbcon.cursor()
sql_st='''
          insert into employees values(101,'rahul',45000.00);
        '''
cursor.execute(sql_st)
dbcon.commit()