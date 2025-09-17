import json
fp=open('emp.json','r')
employees=json.load(fp)
print(type(employees))
print(employees)

#if wanted to itterate the array
for emp in employees:
    print(emp['ename'])