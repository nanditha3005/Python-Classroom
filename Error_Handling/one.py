#without error handling

# print(10/5)  #2.0
# print(10/2)   #5.0
# print(10/0)    #zero-division error
# print(10/1)

#with error handling
print(10/5)    #2.0                     
print(10/2)    #5.0
try:
    print(10/0)     #cant divide by zero

except:
    print("cant divide by zero")

print(10/1)        #10.0