#create dict object
emp={
    'eid':101,
    'ename':'Rahul',
    'esal':45000.45,
    'email':'rg@ibm.com',
}
#read
print(emp)
#how to read dict values? uisng key
print(emp['eid'])
print(emp['ename'])
print(emp['esal'])
print(emp['email'])
print(emp['loc'])  #keyError
#update
print("*Updating")
emp['ename'] = "Rahul Gandhi"
emp['avail']=False     #new key:value pair added
print(emp)
