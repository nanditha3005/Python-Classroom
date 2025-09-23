#without error handling
# fp=None
# fp=open('abc.txt','r')
# data=fp.read()
# print(data)

# fp.close()



#with error Handling
fp=None
try:
    fp=open("abc.txt",'r')
except FileNotFoundError as err:
    fp=open('default.txt','r')
    print(err)
    data=fp.read()
    print(data)

finally:
    print('Finally block  exceute always')
    fp.close()

