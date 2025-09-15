fp1=open('data.txt','r')
data=fp1.read()


fp2=open('abc.txt','w')  #it overwrites
#fp2=open('abc.txt','a')   #it doesnt overwrite ,
fp2.write(data)
print ('new file created')