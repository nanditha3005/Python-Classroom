employees=[
    {'eid':101,'ename':'Rahul','gender':'Male'},
    {'eid':102,'ename':'Priyanka','gender':'Female'},
    {'eid':103,'ename':'Sonia','gender':'Female'},
]
#print employee names

for employee in employees:
    print("Employee Name:", employee['ename'])
    print('Employee Id:', employee['eid'])
    print('Employee Gender:',employee['gender'])