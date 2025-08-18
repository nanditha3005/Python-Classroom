#how to read dict values: using keys
emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45

}

print(emp['eid'])
print(emp['ename'])
print(emp['esal'])
print(emp['loc'])  #no such key so key error occurs

#update 
emp['ename']='Rahul ji'
emp['email']='rahul@gmail.com'
print(emp)


#delete
del (emp['esal'])