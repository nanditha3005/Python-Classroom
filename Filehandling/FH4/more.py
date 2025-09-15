fp1=open('abc.txt','r')
fp2=open('data.txt','w')

print(fp1.readable())   #true
print(fp1.writable())    #false
print(fp1.name)         #abc.txt
print(fp1.mode)          #r(read)
print(fp1.closed)       #false

print(fp2.readable())    #false
print(fp2.writable())    #true
print(fp2.name)          #data.txt
print(fp2.mode)          #w(write)
print(fp2.closed)        #false