import requests,mysql.connector,json,csv 

#extract
resonse_data=requests.get('https://dummyjson.com/users')
users=resonse_data.json()['users']

#Transform
new_users=[]
employees=[]

for user in users:
    new_users.append((user['id'],user['username'],user['email'],user['gender']))
    employees.append({'emp_id':user['id'],'ename':user['username'],'gender':user['gender']})
print(new_users)


#load
dbcon=None
try:
    dbcon=mysql.connector.connect(host="localhost",user="root", password="root",database="dbfour")
    cursor=dbcon.cursor()
    sql_st='''
            insert into users()
            values
            (%s,%s,%s,%s)
            ''' 
    cursor.executemany(sql_st,new_users)
    dbcon.commit()
    print("Data inserted")


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



# employees=[]

# employees.append({'emp_id':user['id'],'ename':user['username'],'gender':user['gender']})


































































































































































































































































