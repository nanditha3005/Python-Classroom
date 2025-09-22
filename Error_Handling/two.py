# a=int(input("Enter First Number:"))
# b=int(input("Enter Second Number:"))
# print(a/b)
# print("Good Morning")


#a=10 b=2   5.0
#a=rahul     ValueError: invalid literal for int() with base 10: ' rahul'
#a=10  b=0    zero division error

#with error handling

try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    print(a/b)
except ValueError as ve:
    print(ve)

except ZeroDivisionError as pr:
    print(pr)

print('GM')

#output:
#case-1
# Enter First Number rahul
# invalid literal for int() with base 10: 'rahul'
# GM

#case-2
#Enter First Number 10
# Enter Second Number 2
# 5.0
# GM

#case-3
#Enter First Number:10
# Enter Second Number:0
# division by zero
# GM

