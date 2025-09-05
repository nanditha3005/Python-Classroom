#pop
numbers=[10,20,30,10,8]
numbers.pop()
print(numbers)

#remove -specified one
numbers.remove(30)
print(numbers)

#clear --delete elements
numbers.clear()
print(numbers)

#del   --delete entire numbers element only
del numbers
print(numbers)          #NameError: name 'numbers' is not defined