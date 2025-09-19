# def division(a,b):
#     print(a/b)

# division(10,5)   #2.0
# division(10,1)   #10.0
# division(10,0)   #zero divison error
# division(10,2)   #not exceutes as error occurs


def smart_div(func):
    def inner(a,b):
        if b==0:
            print("Cannot divide by 0")
        else:
            return func(a,b)
    return inner

@smart_div
def division(a,b):
    print(a/b)

division(10,5)     #2.0
division(10,1)     #10.0
division(10,0)     #Cannot divide by 0
division(10,2)     #5.0