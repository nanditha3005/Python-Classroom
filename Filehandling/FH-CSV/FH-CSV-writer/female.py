import json,csv

fp1=open('emp.json','r')
fp2=open('male.csv','w', newline="")
employees=json.load(fp1)
# print(employees)

male_employees=[]
for emp in employees:
    if emp['gender']=='Female':
        male_employees.append(emp['gender'])


cw=csv.writer(fp2)             
cw.writerow(['gender'])
cw.writerows(male_employees)
print('New CSV File Created')
