#read users.json file and write all female users into new json file i.e. female.json
import json
fp1=open('users.json','r')
fp2=open('female.json','w')

users=json.load(fp1)

female_users=[]
for user in users:
    if user['gender']=='Female':
        female_users.append(user)

print(len(female_users))
json.dump(female_users,fp2)
print('New Json File Created')

fp1.close()
fp2.close()

