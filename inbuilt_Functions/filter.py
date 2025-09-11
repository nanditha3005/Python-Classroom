#normal method
numbers=[11,18,7,31,8,232,454]
#print all even numbers only
even_nos=[]
for num in numbers:
    if num%2==0:
        even_nos.append(num)
print(even_nos)
#----------------------
#using filter
numbers=[11,18,7,31,8,232,454]
def even_nos(num):
    return num%2==0

filter_obj=filter(even_nos,numbers)
even_nos=list(filter_obj) 
print(filter_obj)
#-------------------------
#using lambda

numbers=[11,18,7,31,8,232,454]
data=filter(lambda num:num%2==0 , numbers)
print(data)
#-----------
#using lambda in short form
print(list(filter(lambda x:x%2==0 , [11,18,7,31,8,232,454])))