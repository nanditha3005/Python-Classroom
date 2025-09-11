  #    collect all usernames ,thier name start with 'R'

unames=["sonia","rahul","priyanka","ramya"]
new_users=[]
#using normal basic one
for uname in unames:
    if uname.startswith('r'):
        new_users.append(uname)

print(uname)
print(new_users)

#------------------
#using filter
def checkname(name):
    return name.startswith('r')

new_users=list(filter(checkname,unames))

print(uname)
print(new_users)

#--------------------
#using filter with lambda
new_users=list(filter(lambda name:name.startswith('r'),unames))

print(uname)
print(new_users)
