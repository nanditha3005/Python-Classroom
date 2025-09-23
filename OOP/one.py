class Account:
    pass

a1=Account()
a2=Account()
a3=Account()
a4=Account()
print(a1)            #<__main__.Account object at 0x000002B979AC7FD0>
print(a2)            #<__main__.Account object at 0x000002B979AC7F40>
print(a3)            #<__main__.Account object at 0x000002B979AC7F10>
print(a4)            #<__main__.Account object at 0x000002B979AC7EE0>
print(id(a1))          #2995633553360
print(id(a2))        #2995633553216
print(id(a3))       #2995633553168
print(id(a4))      #2995633553120
