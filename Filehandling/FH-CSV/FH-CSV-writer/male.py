import json,csv
fp1=open('emp.json','r')
fp2=open('male.csv','w', newline="")
employees=json.load(fp1)
# print(employees)

male_employees=[]
for emp in employees:
    if emp['gender']=='Male':
        male_employees.append(emp['gender'])


cw=csv.writer(fp2)             
cw.writerow([emp['gender']])
cw.writerows(male_employees)
print('New CSV File Created')

    
# import json,csv
# fp1=open('users.json','r')
# fp2=open('users.csv','w',newline="")
# users=json.load(fp1)
# #print(users)
# new_users=[]
# for user in users:
#     new_users.append((user['uid'],user['uname'],user['gender']))

# # print(new_users)
# cw=csv.writer(fp2)             #cw-csv writter
# cw.writerow(['uid' ,'uname' ,'gender'])
# cw.writerows(new_users)
# print('New CSV File Created')

    


