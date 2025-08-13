#create -variable
eid=101;

#read-variable
print(eid)

#update 
eid="one hundred one"
print(eid)

#delete
del eid
print (eid)  #Name error will come if deleted and then printed
