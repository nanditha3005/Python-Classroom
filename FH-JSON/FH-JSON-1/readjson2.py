#print the available names
import json
fp=open('emp.json','r')
employees=json.load(fp)
print(type(employees))
print(employees)

for emp in employees:
    if emp["avail"]==True:
        print(emp["avail"])



   