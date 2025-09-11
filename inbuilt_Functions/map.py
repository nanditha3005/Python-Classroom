numbers=[10,20,30,40]
#  create new list of numbers by adding  +1 to existing list

new_numbers=[]
for num in numbers:
    new_numbers.append(num+1)

print(new_numbers)
#------------------
 #using map function
numbers=[10,20,30,40]
def addplusone(num):
    return num+1

map_obj=map(addplusone,numbers) #map expecting one function and sequence
new_numbers=list(map_obj)
print(new_numbers)
#-----------------
#using lamda function(no def keywprd ,no return)
numbers=[10,20,30,40]
map_obj=map(lambda num: num+1 ,numbers)

new_numbers=list(map_obj)
print(new_numbers)
#----------------------------

#simple way of lamda
print(list(map(lambda x:x+1 ,[10,20,30,40] ) ))