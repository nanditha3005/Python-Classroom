numbers=[1,2,3,4]
#create new list for every number by adding +1

new_numbers=[]
for num in numbers:
    new_numbers.append(num+1)
print(new_numbers)

#using map
new_numbers=list(map(lambda n:n+1 ,numbers))
print(new_numbers)

#using list comprehension:as this is using map every element gets changed so no need to mention the condition

new_numbers2=[num+1   for num in numbers ]
print(new_numbers2)