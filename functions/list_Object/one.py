numbers=[10,20,30,10,8]
#create-methods
#read--methods
#update -methods
#delete -methods
print(numbers)
print(numbers.index(20))
#print(numbers.index(200))  #ValueError: 200 is not in list

#count
print(numbers.count(10))

#append:
numbers.append(25)
print('after appending element')
print(numbers)

#insert:
numbers.insert(1,2)

#sort:
numbers.sort()
print(numbers)