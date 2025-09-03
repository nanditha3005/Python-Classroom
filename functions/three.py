def add(a,b):
    print(a+b)

add(10,20)
add(1,2)
add(10,20,30)  #TypeError: add() takes 2 positional arguments but 3 were given
add("Rahul",10)   #TypeError: can only concatenate str (not "int") to str

add('rahul','Gandhi')