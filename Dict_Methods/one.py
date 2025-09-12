#dict-group of key-value pair as one entity
    #-whwere 
#    -index is not possible
#    -dict is mutable object
emp={
    'eid':101,
    'ename':'rahul',
    'esal':21000
}
#print all emp-values
print(emp['eid'])
print(emp['ename'])
print(emp['esal'])
print(emp['loc'])        # KeyError: 'loc'