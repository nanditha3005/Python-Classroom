emp_data={
    'employees':[
        {'eid':101,'ename':'rahul'},
        {'eid':102,'ename':'sonia'},
        {'eid':103,'ename':'priyanka'},
    ]
}
employees=emp_data['employees']

for emp in employees:
    print(emp['eid'])

for emp in emp_data['employees']:
    print(emp['ename'])