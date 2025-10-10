import requests,mysql.connector,json,csv
#extract
response_data=requests.get('https://dummyjson.com/users')
users=response_data.json()['users']
#transform
new_users=[]
employees=[]
for user in users:
    new_users.append((user['id'],user['username'],user['email'],user['gender']))
    employees.append({'emp_id':user['id'],'ename':user['username'],'gender':user['gender']})
print(new_users)
#load
dbcon=None
try:
    dbcon=mysql.connector.connect(host="localhost",
                              user="root",
                              password="root",
                              database="sixdb"

                              )
    cursor=dbcon.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT ,
            username VARCHAR(255),
            email VARCHAR(255),
            gender VARCHAR(10)
        )
    """)
    sql_st='''
        insert into users(id,username,email,gender) values (%s,%s,%s,%s)
       '''
    cursor.executemany(sql_st,new_users)
    dbcon.commit()
    print('data inserted')

except mysql.connector.Error as err:
    print(err)

finally:
    pass

fp1=open('user.csv','w',newline='')
cw=csv.writer(fp1)
cw.writerow(['user_id','name','email','gender'])
cw.writerows(new_users)
print('new csv file created')

fp2=open('emp.json','w')
json.dump(employees,fp2, indent=4)
print('new json file created')




